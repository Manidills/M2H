from models.call2llm import get_response
import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic
import os 
import osmnx
import geopandas as gpd 
import matplotlib.pyplot as plt 
from ipywidgets import embed
import streamlit.components.v1 as components
import pydeck as pdk



def plan():
    st.title("Create Your Travel Plan Here")

    st.markdown("##")

    c1,c2 = st.columns((2,2))
    with c1:
        num_days = st.number_input("Number of Travel Days", min_value=1, value=1)
    with c2:
        # Area input
        area = st.text_input("Area", )
        
    # Submit button
    submit_button = st.button("Create")
    
    if submit_button:
        response_placeholder = st.empty()
        response = get_response( f" have {num_days} days of holidays and i want to spend some time in {area} health tourism related destination. can you share a daily activiest and transportation details plan sheet ?", response_placeholder)

