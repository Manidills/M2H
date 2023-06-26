from models.call2llm import get_response
import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic

# Set the initial location to the Montenegro Airport
start_location = (42.3599, 19.2511)

# Define the locations and their coordinates
locations = {
    "Airport": (42.3599, 19.2511),
    "Durmitor National Park": (43.1333, 19.0323),
    "Ada Bojana": (41.8817, 19.3364),
    "Turkish Bathhouse": (42.4342, 18.7694),
    "Medical Centar Budva": (42.2814, 18.8438),
    "Dental Montenegro": (42.2790, 18.8492),
    "Spa Medica": (42.2937, 18.8394),
    "Herceg Novi": (42.4574, 18.5375),
    "KAMALAYA SPA BAR":(42.0934556,19.1305129),
    "KATHARSIS WELLNESS & HEALTH, Budva":(42.2869113,18.8412352)
}

# Define health tour related summaries for each location
location_summaries = {
    "Airport": "Podgorica airport",
    "Durmitor National Park": "Durmitor National Park offers various wellness and outdoor activities, including hiking, trekking, and breathtaking natural landscapes.",
    "Ada Bojana": "Ada Bojana is a popular health tourism destination known for its pristine beaches, surfing, and wellness resorts.",
    "Turkish Bathhouse": "The Turkish Bathhouse is a traditional spa where visitors can enjoy relaxing baths, massages, and rejuvenating treatments.",
    "Medical Centar Budva": "Medical Centar Budva is a leading healthcare facility in Montenegro, offering a wide range of medical and wellness services.",
    "Dental Montenegro": "Dental Montenegro is a specialized dental clinic known for its high-quality dental treatments and cosmetic dentistry services.",
    "Spa Medica": "Spa Medica is a renowned wellness center providing a variety of spa treatments, beauty therapies, and holistic wellness programs.",
    "Herceg Novi": "Herceg Novi is a coastal town known for its health resorts, thermal springs, and wellness retreats with stunning sea views.",
    "KAMALAYA SPA BAR": "Offers complete relaxation Thai massage makes way to total relaxation clearing the blocked energetically meridians with stretching and tender pressuring.",
    "KATHARSIS WELLNESS & HEALTH, Budva": "Katharsis Wellness & Spa Center is located at the most beautiful part of the Adriatic coast, surrounded by rocky mountains and stunning nature. The center was first to merge holistic health approach and traditional medical methods in Montenegro. Make a step forward to make your body healthier, to feel and look better."
}

# Create a map centered around the start location
map_center = start_location
m = folium.Map(location=map_center, zoom_start=7)

# Add markers for all the locations
for location, coordinates in locations.items():
    folium.Marker(coordinates, popup=location).add_to(m)

polylines = []

# Create a route connecting the start and stop destinations
def create_route(start, stop):
    start_coords = locations[start]
    stop_coords = locations[stop]


    polylines.clear()

    route = [start_coords, stop_coords]
    polyline = folium.PolyLine(locations=route, color='blue')
    polyline.add_to(m)
    polylines.append(polyline)
# Calculate the shortest road route
def calculate_shortest_route(start, stop):
    start_coords = locations[start]
    stop_coords = locations[stop]
    route_distance = geodesic(start_coords, stop_coords).km
    return route_distance
def health_tour_map():
    # Display the map in Streamlit
    st.title("Montenegro Health Destinations")

    col1,col2 = st.columns((2,2))
    # Select start and stop destinations
    with col1:
        start_destination = st.selectbox("Start Destination", list(locations.keys()))
    with col2:
        stop_destination = st.selectbox("Stop Destination", list(locations.keys()))

    # Create the route based on the selected destinations
    create_route(start_destination, stop_destination)

    # Calculate and display the shortest road route
    route_distance = calculate_shortest_route(start_destination, stop_destination)
    st.write(f"Shortest Road Route Distance: {route_distance:.2f} km")

    # Display summary for the selected destination
    if st.button("Show Destination Summary"):
        if start_destination == stop_destination:
            st.write("Start and stop destinations cannot be the same.")
        else:
            selected_destination = locations[stop_destination]
            st.subheader(stop_destination)
            st.write("Latitude:", selected_destination[0])
            st.write("Longitude:", selected_destination[1])
            response_placeholder = st.empty()
            response = get_response( f"can you suggest the best route to travel between {start_destination} to {stop_destination}", response_placeholder)
            # st.write(response)
            # Add more information about the destination here if desired
            
            st.info(location_summaries[stop_destination])
   
    # Render the map
    folium_static(m,width=800, height=800)

    