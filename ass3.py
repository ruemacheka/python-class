"""
Assignment 3: API Consumption with Requests
Objective: Call a public API and display data
"""

# Step 1: Choose a public API (e.g., OpenWeatherMap, NewsAPI, CoinGecko)
# We'll use the OpenWeatherMap API which is popular and easy to use
# You need to sign up for a free API key at https://openweathermap.org/api
# The API key is required to authenticate your requests
#I have signed up for an API key and will use it in the code below
#Assignment 3: API Consumption with Requests
#Objective: Call a public API and display data

# Step 1: Choose a public API (e.g., OpenWeatherMap, NewsAPI, CoinGecko)
# Step 2: Read documentation and get the API endpoint
# Step 3: Use requests.get() to fetch data in JSON format
# Step 4: Extract and print key pieces of information (e.g., current temperature, top news title)

#solution 

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