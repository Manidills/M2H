import tempfile
import os
#from db import insert_wallet
from models.extract_text import extract_text_from_pdf
from models.call2llm import get_response, get_continued_response
# from ipfs import estuary, lighthouse, nft_port, store_on_ipfs, w3_store
# from nft_store import nft_storage_store  # Import specific functions instead of importing everything from call2llm
import streamlit as st
from wallet_connect import wallet_connect
# from streamlit_app import wallet_con


def ask(wallet):
    st.title("Enquire Based on Your Medical Reports")
    with st.form("my_form"):
        uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type=["pdf"])
        pdf_files = []

        # Process uploaded PDFs
        if uploaded_files:
            for uploaded_file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_file_path = temp_file.name

                pdf_files.append((uploaded_file.name, temp_file_path))
            
            # Two-column layout for start and end pages
            col1, col2 = st.columns(2)

            # Convert PDFs to text
            converted_texts = []
            for i, (file_name, file_path) in enumerate(pdf_files):
                # Input fields for start and end pages
                with col1:
                    start_page = st.number_input(f"Start Page ({file_name})", min_value=1, value=1, key=f"start_page_{i}")
                with col2:
                    end_page = st.number_input(f"End Page ({file_name})", min_value=start_page, value=start_page, key=f"end_page_{i}")

                # Convert PDF to text
                text = extract_text_from_pdf(file_path, start_page, end_page)
                converted_texts.append(text)
        query = st.text_input("Enter your question")
        ask_pdf = st.form_submit_button("Ask")

        if ask_pdf :
            response_placeholder = st.empty()
            combined_text = "\n".join(converted_texts)
            response = ""

            if query:
                  response = get_response(combined_text + query, response_placeholder)
            else:
                    response = get_response(combined_text + "lets play the game, what to know whats is problem detected in this report and list some of common clinic names from montenegro upto your knowledge then list out some names of the spa or wellness service may works for this conditions in montenegro upto your knowledge", response_placeholder)
        
            with tempfile.NamedTemporaryFile(suffix=".txt",delete=False) as temp:
                        with open(temp.name, 'w') as temp:
                            temp.write(response) 
           

                # Delete temporary files
            for _, file_path in pdf_files:
                os.remove(file_path)

            if wallet != None:
                st.success("Pushed to DB")

 


