"""
Lesson 6: Take-Home Exercise - Data Science with a Kaggle Dataset
------------------------------------------------------------------
Objective:
- Find and download a CSV dataset from Kaggle (any topic of interest).
- Load and inspect the dataset.
- Clean and preprocess the dataset.
- Perform exploratory data analysis (EDA).
- Generate at least two visualizations.

Instructions:
1. Visit https://www.kaggle.com and find a dataset you are interested in.
2. Download the dataset (must be a CSV file).
3. Place the CSV file in the same directory as this script.
4. Update the `file_name` variable with the correct filename.
5. Run this script to complete the exercise.
"""

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Ask the user to enter the dataset file name
file_name = input("Enter the name of your Kaggle dataset CSV file (including .csv extension): ")

try:
    # Step 2: Load the dataset
    df = pd.read_csv(file_name)
    print("\nDataset successfully loaded!")

    # Step 3: Display basic information about the dataset
    print("\n========== Dataset Overview ==========")
    print("\nFirst 5 Rows:\n", df.head())
    print("\nBasic Info:\n")
    print(df.info())
    print("\nMissing Values:\n", df.isnull().sum())

    # TODO: Step 4: Data Cleaning - Ask the user to fill or drop missing values
    

    # TODO: Step 5: Ask the user to select a column for descriptive statistics


    # TODO: Step 6: Ask the user to choose a visualization type


except FileNotFoundError:
    print("\nError: File not found. Please ensure the dataset file is in the same directory as this script.")

except pd.errors.EmptyDataError:
    print("\nError: The file is empty or not a valid CSV format.")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
