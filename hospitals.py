from models.call2llm import get_response
import streamlit as st
import pandas as pd
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

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


def hospitals():
    st.title("Health Care Details")

    hos = st.radio("Major Health Care",('Public', 'Private'), horizontal=True)

    st.markdown("##")
    if hos == 'Public':
        df = pd.read_csv('public.csv')
        st.dataframe(df,use_container_width=True)
        csv = convert_df(df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )
   
    elif hos == 'Private':
        df = pd.read_csv('private.csv')
        st.dataframe(df,use_container_width=True)
        csv = convert_df(df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )
    
    st.markdown('##')
    AOI = 'Montenegro'
    aoi_gdf = osmnx.geocode_to_gdf(AOI)
    basemap = aoi_gdf.explore(color='lightblue')

   
    try:

        hospitals = osmnx.geometries_from_polygon(polygon = aoi_gdf.geometry.geometry.unary_union,
                                            tags = {'amenity': 'hospital'})
                                            
        folium_static(hospitals.explore(tooltip=['name'],
                    color = 'green',
                    marker_type=folium.Marker(),
                    min_zoom = 8
                    ), width=800)
    except:
        st.info("No Preview avilable")

    
    with open("modified_file.csv", "rb") as template_file:
        template_byte = template_file.read()

    st.download_button(label="Click to Download Entire Dataset",
                        data=template_byte,
                        file_name="Database.csv",
                        mime='application/octet-stream')
    st.markdown("##")

    st.subheader("Hospital Info")

    hos = st.selectbox("Hospitals", df['Name of medical facility'].tolist())
    if st.button("Explore"):
        response_placeholder = st.empty()
        response = get_response(f'"{hos}" clinic, can you give some details about this clinic in montenegro and list some common service provided ?',response_placeholder)




    


    

    






