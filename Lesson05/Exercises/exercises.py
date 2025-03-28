#!/usr/bin/env python3
"""
In-Class Exercises for Lesson 5: Python Modules Integration

This script contains four exercises:
  1. API Data Fetch and Conversion to CSV
  2. Directory Analyzer and File Manipulation
  3. Data Processing Pipeline (CSV to JSON and optional pandas analysis)

Each exercise demonstrates how to integrate various Python modules:
  - File handling (open, read, write)
  - os module for file system operations
  - requests for web API calls
  - csv and json for data processing
  - pandas and numpy for data analysis

Instructions:
  - Run the script to see each exercise executed in sequence.
  - Review the inline comments and pseudo-code for guidance.
  - Modify and extend the exercises to experiment further.

"""

import os
import json
import csv
import requests  # Ensure this package is installed: pip install requests

# Optional: Import pandas if available (install with: pip install pandas)
try:
    import pandas as pd
except ImportError:
    pd = None

# Change the working directory to the current file's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ================================
# Exercise 1: API Data Fetch and Conversion to CSV
# ================================
"""
Exercise 1: API Data Fetch and Conversion to CSV

Task:
  - Use the requests module to fetch JSON data from a public API (e.g., https://jsonplaceholder.typicode.com/posts).
  - Save the fetched JSON data to a file named 'posts.json'.
  - Read 'posts.json' and convert the data into a CSV file named 'posts.csv', including only the fields: userId, id, and title.
"""

def exercise_1():
    print("\n--- Exercise 1: API Data Fetch and CSV Conversion ---")
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        # Step 1: Fetch data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        posts = response.json()
    except Exception as e:
        print("Error fetching data:", e)
        return

    # Step 2: Save the JSON data to 'posts.json'
    # TODO: Write the JSON data to a file named 'posts.json'

    # Step 3: Load the JSON data from file
    # TODO: Read the JSON data from 'posts.json'

    # Step 4: Write the selected fields to 'posts.csv'
    # TODO: Write the selected fields to a CSV file named 'posts.csv'

    print("Converted data saved to 'posts.csv'.")


# ================================
# Exercise 2: Directory Analyzer and File Manipulation
# ================================
"""
Exercise 2: Directory Analyzer and File Manipulation

Task:
  - Check if a directory named 'data' exists; if not, create it.
  - Within the 'data' directory, create three text files ('file1.txt', 'file2.txt', 'file3.txt') containing sample content.
  - List all files in the 'data' directory and print each file's name along with its file size (in bytes).
"""

def exercise_2():
    print("\n--- Exercise 2: Directory Analyzer and File Manipulation ---")
    dir_name = 'data'
    
    # Step 1: Ensure 'data' directory exists
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created.")
    else:
        print(f"Directory '{dir_name}' already exists.")

    # Step 2: Create three text files with sample content
    sample_files = ['file1.txt', 'file2.txt', 'file3.txt']
    sample_text = "This is a sample text for {}."
    for filename in sample_files:
        file_path = os.path.join(dir_name, filename)
        # TODO: Write sample text to file
        

    # Step 3: List files in 'data' and display file sizes
    print("\nListing files and their sizes in 'data':")
    for item in os.listdir(dir_name):
        file_path = os.path.join(dir_name, item)
        # TODO: Check if the item is a file
        # TODO: Calculate file size in bytes


# ================================
# Exercise 3: Data Processing Pipeline
# ================================
"""
Exercise 3: Data Processing Pipeline

Task:
  - Create a CSV file named 'students.csv' with headers: Name, Age, Grade, and populate it with sample data for at least 5 students.
  - Read 'students.csv' and convert each row into a dictionary, then write the list of dictionaries to a JSON file named 'students.json'.
  - Using pandas, load the CSV into a DataFrame, compute the average Age and Grade, and print the results.
"""

def exercise_3():
    print("\n--- Exercise 3: Data Processing Pipeline ---")
    csv_filename = 'students.csv'
    json_filename = 'students.json'
    
    # Step 1: Create 'students.csv' with sample data
    header = ['Name', 'Age', 'Grade']
    student_data = [
        ['Alice', '22', '88'],
        ['Bob', '24', '92'],
        ['Charlie', '23', '85'],
        ['Diana', '21', '90'],
        ['Edward', '25', '87']
    ]
    with open(csv_filename, 'w', newline='') as csvfile:
        # TODO: Write header and rows to the CSV file
        pass


    # Step 2: Read 'students.csv' and convert rows to dictionaries
    students = []
    with open(csv_filename, 'r') as csvfile:
        # TODO: Read the CSV file and convert each row to a dictionary
        pass

    # Step 3: Write the list of dictionaries to 'students.json'
    with open(json_filename, 'w') as jsonfile:
        # TODO: Write the list of dictionaries to a JSON file
        pass

    # Step 4: Analyze the CSV data using pandas
    try:
        import pandas as pd
    except ImportError:
        pd = None

    if pd:
        # TODO: Load the CSV data into a DataFrame using pandas
        # TODO: Compute average Age and Grade using pandas
        pass
    else:
        print("Pandas is not installed. Skipping data analysis using pandas.")


# ================================
# Main Execution for All Exercises
# ================================
def main_exercises():
    exercise_1()
    exercise_2()
    exercise_3()

if __name__ == '__main__':
    main_exercises()
