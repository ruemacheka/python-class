
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
