import os
from dotenv import load_dotenv
import requests
import streamlit as st

load_dotenv('weather.env')  # Load environment variables from your file

api_key = os.getenv('API_KEY')  # Get the API key

st.title("🌤️ Weather Forecast App")

city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    if city == "":
        st.warning("Please enter a city name")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            st.error("City not found")
        else:
            st.success(f"🌡️ Temperature: {data['main']['temp']} °C")
            st.info(f"💧 Humidity: {data['main']['humidity']}%")
            st.write(f"☁️ Condition: {data['weather'][0]['description']}")