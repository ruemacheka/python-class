#Assignment 4: Build a Mini Flask App Using Scraped or API Data
#Objective: Create a simple Flask app with two routes:
         #- '/'       => display homepage
         #- '/data'   => show scraped/API data

# Step 1: Setup Flask app in a file named app.py
# Step 2: Create a route for homepage with a welcome message
# Step 3: Create another route that displays the API or scraped data (can use templates or just return strings)
# Step 4: Run Flask server and test in browser

from flask import Flask
import requests
from datetime import datetime

# Create the Flask application
app = Flask(__name__)

# Function to get weather data from OpenWeatherMap API
def get_weather_data():
    API_KEY = "94bc0282abeee15e1ea6906593ea75c9"
    city = "Austin"
    country_code = "us"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Route for homepage with a welcome message
@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Welcome to Weather App</h1>
    <p>This is a simple Flask application that demonstrates API integration.</p>
    <p>Current server time: {current_time}</p>
    <p><a href="/data">View Weather Data</a></p>
    """

# Route that displays the API data
@app.route('/data')
def data():
    weather_data = get_weather_data()
    if "error" in weather_data:
        return f"<h1>Error</h1><p>Could not fetch weather data. Please try again later.</p>"
    
    return f"""
    <h1>Weather in {weather_data['name']}, {weather_data['sys']['country']}</h1>
    <p><b>Temperature:</b> {weather_data['main']['temp']}°C</p>
    <p><b>Feels like:</b> {weather_data['main']['feels_like']}°C</p>
    <p><b>Weather condition:</b> {weather_data['weather'][0]['description']}</p>
    <p><b>Humidity:</b> {weather_data['main']['humidity']}%</p>
    <p><b>Wind speed:</b> {weather_data['wind']['speed']} m/s</p>
    <p><a href="/">Back to Home</a></p>
    """

# Run the app
if __name__ == '__main__':
    app.run(debug=True)