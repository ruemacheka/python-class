#!/usr/bin/env python3
"""
Cheat Sheet for Common Python Modules

Modules Covered:
  - os: Operating system interface functions.
  - Basic File I/O: Reading and writing files.
  - csv: Reading from and writing to CSV files.
  - json: Working with JSON data.
  - requests: Making HTTP requests.

This cheat sheet demonstrates common usages and functions for each module.
"""

import os
import csv
import json
import requests

# ------------------------------
# os Module Cheat Sheet
# ------------------------------
def cheat_os():
    print("\n--- os Module Cheat Sheet ---")
    
    # Get current working directory
    cwd = os.getcwd()
    print("Current Working Directory:", cwd)
    
    # List all files and directories in the current directory
    items = os.listdir(cwd)
    print("Items in Directory:")
    for item in items:
        print("  ", item)

    # Get file size
    file_path = os.path.join(cwd, "cheatsheet.General.py")
    file_size = os.path.getsize(file_path)
    print(f"Size of '{file_path}': {file_size} bytes")
    
    # Join paths in a platform-independent way
    new_path = os.path.join(cwd, "example_folder")
    print("Joined Path:", new_path)
    
    # Check if a path exists
    exists = os.path.exists(new_path)
    print(f"Does '{new_path}' exist? {exists}")
    
    # Create a directory if it doesn't exist
    if not exists:
        os.mkdir(new_path)
        print(f"Created directory: {new_path}")
    else:
        print(f"Directory already exists: {new_path}")
    
    # Remove a directory (use with caution)
    # os.rmdir(new_path)  # Uncomment to remove the directory if empty

# ------------------------------
# Basic File I/O Cheat Sheet
# ------------------------------
def cheat_file_io():
    print("\n--- Basic File I/O Cheat Sheet ---")
    filename = "cheatsheet_example.txt"
    content = "Hello, this is a file I/O example.\nLine 2 of the file."
    
    # Write to a file
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Wrote content to {filename}")
    
    # Read from a file
    with open(filename, 'r') as file:
        read_content = file.read()
    print("Content read from file:")
    print(read_content)
    
    # Append to a file
    with open(filename, 'a') as file:
        file.write("\nAppended line.")
    print("Appended content to file.")
    
    # Read file line by line
    print("Reading file line by line:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# ------------------------------
# csv Module Cheat Sheet
# ------------------------------
def cheat_csv():
    print("\n--- csv Module Cheat Sheet ---")
    csv_filename = "cheatsheet_data.csv"
    
    # Sample data to write
    header = ["Name", "Age", "City"]
    rows = [
        ["Alice", "30", "New York"],
        ["Bob", "25", "Los Angeles"],
        ["Charlie", "35", "Chicago"]
    ]
    
    # Write CSV using csv.writer
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)   # Write header
        writer.writerows(rows)    # Write multiple rows
    print(f"CSV data written to {csv_filename}")
    
    # Read CSV using csv.reader
    print("Reading CSV using csv.reader:")
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    
    # Write CSV using csv.DictWriter
    dict_csv_filename = "cheatsheet_dict_data.csv"
    dict_rows = [
        {"Name": "David", "Age": "28", "City": "Seattle"},
        {"Name": "Eva", "Age": "32", "City": "Boston"}
    ]
    with open(dict_csv_filename, 'w', newline='') as csvfile:
        fieldnames = ["Name", "Age", "City"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dict_rows)
    print(f"CSV (dict) data written to {dict_csv_filename}")
    
    # Read CSV using csv.DictReader
    print("Reading CSV using csv.DictReader:")
    with open(dict_csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

# ------------------------------
# json Module Cheat Sheet
# ------------------------------
def cheat_json():
    print("\n--- json Module Cheat Sheet ---")
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "San Francisco",
        "hobbies": ["reading", "hiking", "coding"]
    }
    json_filename = "cheatsheet_data.json"
    
    # Convert dictionary to JSON string (pretty print)
    json_str = json.dumps(data, indent=4)
    print("JSON string:")
    print(json_str)
    
    # Write JSON to a file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data written to {json_filename}")
    
    # Read JSON from a file
    with open(json_filename, 'r') as json_file:
        loaded_data = json.load(json_file)
    print("Data loaded from JSON file:")
    print(loaded_data)

# ------------------------------
# requests Module Cheat Sheet
# ------------------------------
def cheat_requests():
    print("\n--- requests Module Cheat Sheet ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        # Make a GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Access the response content
        data = response.json()  # Parse JSON response
        print("Response JSON data:")
        print(json.dumps(data, indent=4))
        
        # Additional examples:
        # response.text -> raw text
        # response.status_code -> HTTP status code
        # response.headers -> response headers
        
    except requests.RequestException as e:
        print("An error occurred while making the GET request:", e)

# ------------------------------
# Main Function: Execute Cheat Sheet Examples
# ------------------------------
def main():
    cheat_os()
    cheat_file_io()
    cheat_csv()
    cheat_json()
    cheat_requests()

if __name__ == '__main__':
    main()
