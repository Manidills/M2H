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


list_cities= [
    'Podgorica','Budva', 'Kotor', 'Herceg Novi', 'Tivat', 'ulcinj', 'Cetinje'
]

def explore_cities():
    st.title("Montenegro Major Cities")

    start_destination = st.selectbox("Major Cities", list_cities)

    if st.button("Explore"):
        response_placeholder = st.empty()
        response = get_response( f"create a short summary about history of the {start_destination} and in points explain about the top 3 tourist places, and top  3 health institues with there specail treatments, also in points suggest the routes to near cities with transpotation details and booking links.", response_placeholder)
        st.write("OpenStreetMap is a highly efficient mapping tool that surpasses other alternatives in its ability to capture and visualize essential features such as hospitals, hotels, churches, transportation centers, and more. With its open-source nature, OpenStreetMap boasts an extensive and up-to-date database, constantly enriched by a global community of contributors. This collaborative effort ensures that users have access to accurate and comprehensive information, empowering them to navigate and explore their surroundings with ease. Whether it's finding the nearest healthcare facility, planning accommodation, locating places of worship, or identifying transportation hubs, OpenStreetMap provides a superior mapping experience by delivering precise and relevant details for major points of interest.")

        AOI = f'{start_destination}, Montenegro'
        aoi_gdf = osmnx.geocode_to_gdf(AOI)
        basemap = aoi_gdf.explore(color='lightblue')

        col1, col2 = st.columns((3,2))

        with col1:
            st.subheader("Specialized Health Care")
            try:

                hospitals = osmnx.geometries_from_polygon(polygon = aoi_gdf.geometry.geometry.unary_union,
                                                    tags = {'amenity': 'hospital'})
                                                    
                folium_static(hospitals.explore(tooltip=['name'],
                            color = 'green',
                            marker_type=folium.Marker(),
                            min_zoom = 12
                            ), width=800)
            except:
                st.info("No Preview avilable")
        with col1:
            st.subheader("Rivers Across the city")
            try:
                river = osmnx.geometries_from_polygon(polygon = aoi_gdf.geometry.geometry.unary_union,
                                        tags = {'waterway': 'river'})


                folium_static(river.explore(color = 'blue'), width=800)
            except:
                st.info("No Preview avilable")


        

        with col1:
            st.subheader("Public Railway Stations")
            try:

                pb_transport_tr = osmnx.geometries_from_polygon(polygon = aoi_gdf.geometry.geometry.unary_union,
                                        tags = {'railway': 'station'})

                folium_static(pb_transport_tr.explore(color = 'red'), width=800)

            except:
                st.info("No Preview avilable")
        with col1:
            st.subheader("Hotels Across the city")
            try:
                hotels = osmnx.geometries_from_polygon(polygon = aoi_gdf.geometry.geometry.unary_union,
                                            tags = {'building': "hotel"})

                folium_static(hotels.explore(tooltip=['name'],
                    color = 'purple',
                    min_zoom = 12
                        ), width=800)
            except:
                st.info("No Preview avilable")




        st.markdown("##")
        st.subheader("Fuel Station Across the city")
        try:
        #fuel stations 
            fuel = osmnx.geometries_from_polygon(polygon = aoi_gdf.geometry.geometry.unary_union,
                                                    tags = {'amenity': "fuel"})



            folium_static(fuel.explore(tooltip=['name'],
                            color = 'red',
                        **{'min_zoom':12}
                            ), width=800)
        except:
            st.info("No Preview avilable")
        
    