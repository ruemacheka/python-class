# Lesson 9: In-Class Assignments - Web Scraping, API Integration, and Web App Enhancement
# Course: MSITM 6341 - Python Programming
# Instructor: Dennis Wang
# Format: Python script with commented instructions for students to follow in Visual Studio Code

"""
Assignment 1: Web Scraping with BeautifulSoup
Objective: Extract the latest headlines from a public news website
"""
# Step 1: Import required modules: requests, bs4 (BeautifulSoup)
# Step 2: Send a GET request to https://news.ycombinator.com/
# Step 3: Parse the HTML content and extract the text of the top 5 headlines
# Step 4: Print the headlines to the console

#solution

# Lesson 9: In-Class Assignments - Web Scraping, API Integration, and Web App Enhancement
# Course: MSITM 6341 - Python Programming
# Instructor: Dennis Wang

""" 
Assignment 1: Web Scraping with BeautifulSoup
Objective: Extract the latest headlines from a public news website
"""

# Step 1: Import required modules: requests, bs4 (BeautifulSoup)
import requests
from bs4 import BeautifulSoup

# Step 2: Send a GET request to https://news.ycombinator.com/
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Step 3: Parse the HTML content and extract the text of the top 5 headlines
soup = BeautifulSoup(response.content, 'html.parser')
# Hacker News headlines are in <span class="titleline"> elements
headlines = soup.select('span.titleline > a')

# Step 4: Print the headlines to the console
print("Top 5 Hacker News Headlines:")
for i, headline in enumerate(headlines[:5], 1):
    print(f"{i}. {headline.text}")


"""
Assignment 2: Dynamic Scraping with Selenium (Optional for Advanced Students)
Objective: Scrape content from a dynamically rendered site like Amazon or Instagram search
"""
# Step 1: Install and import selenium and webdriver_manager
# Step 2: Launch a browser using Selenium WebDriver
# Step 3: Navigate to a site (e.g., https://quotes.toscrape.com/js/)
# Step 4: Extract 5 quotes and authors
# Step 5: Print the results



# Step 1: Install and import selenium and webdriver_manager
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Step 2: Launch a browser using Selenium WebDriver
# Set up Chrome options (headless mode is optional but makes it run without UI)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Set up the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 3: Navigate to a site (e.g., https://quotes.toscrape.com/js/)
    driver.get("https://quotes.toscrape.com/js/")
    
    # Wait for JavaScript to load the content
    time.sleep(3)  # Simple wait - in production, use WebDriverWait instead
    
    # Step 4: Extract 5 quotes and authors
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    
    # Step 5: Print the results
    print("Top 5 Quotes and Authors:")
    for i, quote in enumerate(quotes[:5], 1):
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        print(f"{i}. \"{text}\"")
        print(f"   - {author}\n")

finally:
    # Always close the driver to free resources
    driver.quit()

#Assignment 3: API Consumption with Requests
#Objective: Call a public API and display data

# Step 1: Choose a public API (e.g., OpenWeatherMap, NewsAPI, CoinGecko)
# Step 2: Read documentation and get the API endpoint
# Step 3: Use requests.get() to fetch data in JSON format
# Step 4: Extract and print key pieces of information (e.g., current temperature, top news title)

#solution 

"""
Assignment 3: API Consumption with Requests
Objective: Call a public API and display data
"""

# Step 1: Choose a public API (e.g., OpenWeatherMap, NewsAPI, CoinGecko)
# We'll use the OpenWeatherMap API which is popular and easy to use
# You need to sign up for a free API key at https://openweathermap.org/api
# The API key is required to authenticate your requests
#I have signed up for an API key and will use it in the code below


# Step 2: Read documentation and get the API endpoint
import requests
import json

# You would need to sign up for a free API key at https://openweathermap.org/api
# I'm using a placeholder - replace with your actual API key
API_KEY = "94bc0282abeee15e1ea6906593ea75c9"  
city = "Austin"  # Example city
country_code = "us"  # Example country code

# Construct the API endpoint
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_KEY}&units=metric"

# Step 3: Use requests.get() to fetch data in JSON format
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses
    data = response.json()
    
    # Step 4: Extract and print key pieces of information
    print(f"Weather in {city}, {country_code.upper()}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels like: {data['main']['feels_like']}°C")
    print(f"Weather condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind speed: {data['wind']['speed']} m/s")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError as e:
    print(f"Could not find expected data in the response: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Assignment 4: Build a Mini Flask App Using Scraped or API Data
#Objective: Create a simple Flask app with two routes:
         #- '/'       => display homepage
         #- '/data'   => show scraped/API data

# Step 1: Setup Flask app in a file named app.py
# Step 2: Create a route for homepage with a welcome message
# Step 3: Create another route that displays the API or scraped data (can use templates or just return strings)
# Step 4: Run Flask server and test in browser

# Import Flask and other required modules
from flask import Flask
from datetime import datetime
import requests

# Create the Flask app instance
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

#Assignment 5 (Bonus): Flask Data Dashboard
#Objective: Visualize scraped or API data using matplotlib or plotly and embed in Flask

# Step 1: Create a plot or chart from the data
# Step 2: Save the chart as an image or generate HTML (for plotly)
# Step 3: Display it in an HTML template


# Note:
# - Use virtual environments to manage packages (pip install virtualenv)
# - Use .env to store API keys securely (optional)
# - Comment your code and write modular functions
