# 🌦️ Voice-Powered Weather App

## 🎯 Objective
The objective of this project is to extend the **Smart Voice Assistant (Task 1)** by integrating it with the **OpenWeatherMap API**. The app fetches **real-time weather data** based on the user’s spoken city name and narrates the details aloud.

---

## 🛠 Steps Performed
1. Reused functions from Task 1 (`pns()` for text-to-speech + `listen()` for voice input).  
2. Integrated the **OpenWeatherMap API** to fetch live weather data.  
3. Processed the JSON response to extract city, temperature, humidity, wind speed, and weather conditions.  
4. Enhanced the assistant to **speak out the weather details** for a better user experience.  
5. Added error handling to manage invalid inputs or API issues.  

---

## ⚙️ Tools & Libraries Used
- **Python 3.13**  
- `requests` → To make API calls to OpenWeatherMap.  
- `Voice_Assistant` module (from Task 1) → For speaking (`pns`) and listening (`listen`).  
- **OpenWeatherMap API** → To fetch real-time weather data.  

---

## ✅ Outcome
- A fully functional **voice-powered weather app**.  
- Users can simply **say the city name**, and the app will respond with:  
  - Temperature (Current, Feels Like, Min, Max) 🌡️  
  - Humidity 💧  
  - Wind Speed 💨  
  - Weather Type & Condition ☁️  
- Demonstrates **modular coding** by extending Task 1’s functionalities.  

---

✨ This project is part of my **Python Programming Internship at Oasis Infobyte** (Task 4). 
