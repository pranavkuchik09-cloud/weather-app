import streamlit as st
import requests
import matplotlib.pyplot as plt
from datetime import datetime


st.title("🌦 Advanced Weather Forecast App")


city = st.text_input("Enter City Name:")


API_KEY = "f2a9a7458653da936307d73ce02dc494"  
CURRENT_URL = "http://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?"

if city:
    # Current Weather Data
    current_url = CURRENT_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(current_url)
    data = response.json()

    if data["cod"] != "404":
        # Extract current weather
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather = data["weather"][0]["description"]

        st.subheader(f"📍 Weather in {city}")
        st.write(f"🌡 Temperature: {temperature}°C")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"🔽 Pressure: {pressure} hPa")
        st.write(f"☁ Condition: {weather.capitalize()}")

        # Forecast Weather Data
        forecast_url = FORECAST_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        st.subheader("📊 5-Day Forecast")

        
        dates, temps = [], []
        for entry in forecast_data["list"]:
            dt = datetime.fromtimestamp(entry["dt"])
            temp = entry["main"]["temp"]
            dates.append(dt)
            temps.append(temp)

        
        plt.figure(figsize=(10, 4))
        plt.plot(dates, temps, marker="o", linestyle="-", color="b")
        plt.title(f"Temperature Forecast for {city}")
        plt.xlabel("Date & Time")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.grid(True)

        st.pyplot(plt)

    else:
        st.error("City Not Found ❌")
