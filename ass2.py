
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
