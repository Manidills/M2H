from hospitals import hospitals
from models.app_web import ask
import streamlit as st
from tour_city import explore_cities
from tour_map import health_tour_map
from wallet_connect import wallet_connect
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Health tourism",
    page_icon="❄️️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)

def introduction():

    st.write("# Introduction to Montenegro and Health Tourism")

    components.html(
        """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {box-sizing: border-box;}
    body {font-family: Verdana, sans-serif;}
    .mySlides {display: none;}
    img {vertical-align: middle;}

    /* Slideshow container */
    .slideshow-container {
    max-width: 1000px;
    position: relative;
    margin: auto;
    }

    /* Caption text */
    .text {
    color: #f2f2f2;
    font-size: 15px;
    padding: 8px 12px;
    position: absolute;
    bottom: 8px;
    width: 100%;
    text-align: center;
    }

    /* Number text (1/3 etc) */
    .numbertext {
    color: #f2f2f2;
    font-size: 12px;
    padding: 8px 12px;
    position: absolute;
    top: 0;
    }

    /* The dots/bullets/indicators */
    .dot {
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #bbb;
    border-radius: 50%;
    display: inline-block;
    transition: background-color 0.6s ease;
    }

    .active {
    background-color: #717171;
    }

    /* Fading animation */
    .fade {
    animation-name: fade;
    animation-duration: 1.5s;
    }

    @keyframes fade {
    from {opacity: .4} 
    to {opacity: 1}
    }

    /* On smaller screens, decrease text size */
    @media only screen and (max-width: 300px) {
    .text {font-size: 11px}
    }
    </style>
    </head>
    <body>

    <h2>Automatic Slideshow</h2>
    <p>Change image every 2 seconds:</p>

    <div class="slideshow-container">

    <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="https://images.unsplash.com/photo-1632482505390-d1a81a0b8cf0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1584&q=80" style="width:100%">
    <div class="text">Caption Text</div>
    </div>

    <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="https://images.unsplash.com/photo-1651951977276-2f984af7bcbd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1593&q=80">
    <div class="text">Caption Two</div>
    </div>

    <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://images.unsplash.com/photo-1672677119196-448c3660aef7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80" style="width:100%">
    <div class="text">Caption Three</div>
    </div>

    <div class="mySlides fade">
    <div class="numbertext">4 / 4</div>
    <img src="https://images.unsplash.com/photo-1635414729486-6bed04a65c28?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=876&q=80">
    <div class="text">Caption Three</div>
    </div>

    </div>
    <br>

    <div style="text-align:center">
    <span class="dot"></span> 
    <span class="dot"></span> 
    <span class="dot"></span> 
    </div>

    <script>
    let slideIndex = 0;
    showSlides();

    function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
    }
    </script>

    </body>
    </html> 

        """,
        height=400,
    )  

    st.markdown("##")

    st.write("Montenegro, a small country located in Southeast Europe, is renowned for its stunning natural beauty, rich history, and vibrant culture. In recent years, it has also emerged as a popular destination for health tourism, attracting visitors seeking relaxation, rejuvenation, and wellness experiences.")

    st.write("Here are some key points about health tourism in Montenegro:")

    st.write("1. Natural Remedies and Climate: Montenegro boasts a diverse range of natural resources, including mineral-rich thermal waters, healing mud, and fresh mountain air. These resources have been utilized for centuries in traditional treatments and therapies, making the country an ideal destination for health-conscious travelers.")

    st.write("2. Spa and Wellness Centers: Montenegro offers a growing number of world-class spa and wellness centers, providing a wide range of treatments and services. From luxurious resorts to boutique retreats, visitors can indulge in various therapies such as massages, facials, aromatherapy, and hydrotherapy, all designed to promote relaxation and well-being.")

    st.write("3. Wellness and Lifestyle Programs: Many wellness centers in Montenegro offer comprehensive programs that focus on holistic health. These programs often include personalized fitness regimes, nutritional counseling, mindfulness practices, and alternative therapies like yoga and meditation. Visitors can embark on wellness journeys tailored to their specific needs, aiming to improve both physical and mental well-being.")

    st.write("4. Traditional and Modern Approaches: Montenegro's health tourism scene blends traditional healing practices with modern techniques. Visitors can experience ancient therapies like Ayurveda, traditional Chinese medicine, and balneotherapy, alongside cutting-edge treatments utilizing the latest advancements in medical science and technology.")

    st.write("# Wellness and Different Spa Culture Development")

    st.write("Montenegro's wellness and spa culture has witnessed significant development, catering to diverse preferences and interests. Here are some notable aspects:")

    st.write("1. Thermal Spa Resorts: Montenegro is home to several thermal spa resorts, which utilize the healing properties of mineral-rich thermal waters. These resorts offer a range of therapeutic treatments, including mineral baths, mud wraps, and underwater massages. Visitors can unwind and revitalize amidst breathtaking natural surroundings.")

    st.write("2. Seaside Wellness Retreats: With its stunning Adriatic coastline, Montenegro has also developed wellness retreats that combine the benefits of sea air, sunlight, and coastal landscapes. These retreats often include spa facilities, beachside yoga classes, outdoor activities, and healthy cuisine, providing a holistic approach to well-being.")

    st.write("3. Mountain Retreats and Eco-Spas: Montenegro's mountainous terrain offers an opportunity for unique wellness experiences. Mountain retreats and eco-spas provide a tranquil environment for relaxation and introspection. Visitors can enjoy activities such as hiking, meditation in serene natural settings, and treatments inspired by local herbs and botanicals.")

    st.write("4. Cultural Immersion and Wellness: Montenegro's rich cultural heritage is often incorporated into wellness experiences. Visitors can engage in traditional ceremonies, learn about local healing practices, and explore the therapeutic benefits of indigenous herbs and remedies. This integration of culture and wellness offers a deeper understanding of Montenegro's holistic approach to health.")

    st.markdown("##")

    def highlight_country_name(country):
        return f"**{country}**"

    st.write("Here is a list of some countries whose citizens are typically allowed to enter Montenegro without a visa:")

    st.write("European Union (EU) and Schengen Area countries:")
    st.write("Citizens of EU and Schengen Area countries are generally allowed to enter Montenegro without a visa. This includes countries like",
            highlight_country_name("Germany") + ",",
            highlight_country_name("France") + ",",
            highlight_country_name("Italy") + ",",
            highlight_country_name("Spain") + ", and many more.")

    st.write("United States, Canada, Australia, and New Zealand:")
    st.write("Citizens of these countries typically do not require a visa for short visits to Montenegro. This includes",
            highlight_country_name("United States") + ",",
            highlight_country_name("Canada") + ",",
            highlight_country_name("Australia") + ", and",
            highlight_country_name("New Zealand") + ".")

    st.write("United Kingdom:")
    st.write("Despite leaving the EU, citizens of the",
            highlight_country_name("United Kingdom") + " are still allowed visa-free entry to Montenegro for tourism or business purposes.")

    st.write("Russia, Ukraine, and other Commonwealth of Independent States (CIS) countries:")
    st.write("Citizens of certain CIS countries, including",
            highlight_country_name("Russia") + " and",
            highlight_country_name("Ukraine") + ", may enter Montenegro without a visa for a specified period.")

    st.write("Balkan countries:")
    st.write("Citizens of neighboring Balkan countries such as",
            highlight_country_name("Serbia") + ",",
            highlight_country_name("Croatia") + ",",
            highlight_country_name("Bosnia and Herzegovina") + ",",
            highlight_country_name("North Macedonia") + ", and",
            highlight_country_name("Albania") + " usually do not need a visa to enter Montenegro.")

    st.write("Some South American countries:")
    st.write("Citizens of certain South American countries like",
            highlight_country_name("Argentina") + ",",
            highlight_country_name("Brazil") + ", and",
            highlight_country_name("Chile") + " may also be allowed visa-free entry into Montenegro.")

    st.write("Please note that the duration of stay allowed without a visa may vary depending on the country. It is essential to verify the visa requirements for your specific nationality and purpose of travel before making any arrangements.")

    st.video("https://www.youtube.com/watch?v=hdOPWI2Ftgg&ab_channel=WorldWildHearts")

 



st.sidebar.image("bear_snowflake_hello.png")
action = st.sidebar.radio("What action would you like to take?", ("Introduction","Health Care","Cities","Destinations", "Enquire"))

def wallet_con():
    with st.sidebar:
        st.markdown('##')
        wallet = wallet_connect(label="wallet", key='wallet')
        return wallet
    

wallet = wallet_con()



if action == "Destinations":
    health_tour_map()
elif action == 'Cities':
    explore_cities()
elif action == "Health Care":
    hospitals()
elif action == "Enquire":
    ask(wallet)
elif action == "Introduction":
    introduction()
