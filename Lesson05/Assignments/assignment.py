#!/usr/bin/env python3
"""
Take-Class Exercises for Lesson 5: Data Analysis with Pandas and NumPy
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
# Take-Home Exercise: Data Analysis with Pandas and NumPy
# ================================
"""
Take-Home Exercise: Data Analysis with Pandas and NumPy

Task:
  - Create a pandas DataFrame using sample data (e.g., student scores in multiple subjects).
  - Convert selected DataFrame columns to a NumPy array and perform vectorized operations.
  - Compute additional statistics (e.g., average scores per student, overall subject averages).
  - Filter the DataFrame based on computed statistics and display the results.

Steps:
  1. Create a dictionary with sample data and convert it into a DataFrame.
  2. Extract the numerical score columns and convert them into a NumPy array.
  3. Use NumPy to compute the average score per student.
  4. Add the computed average as a new column in the DataFrame.
  5. Compute overall class averages for each subject using pandas.
  6. (Optional) Filter and display students with scores above a certain threshold.
"""

def pandas_exercise():
    print("\n--- Take-Home Exercise: Data Analysis with Pandas and NumPy ---")
    try:
        import pandas as pd
        import numpy as np
    except ImportError as e:
        print("Pandas or NumPy is not installed. Skipping Take-Home Exercise.")
        return

    # Step 1: Create sample data and DataFrame
    data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
        'Math': [88, 92, 79, 85, 90],
        'Science': [91, 85, 88, 90, 86],
        'English': [85, 87, 90, 82, 88]
    }
    # TODO: Load the data into pandas DataFrame and print it
    
    # Step 2: Convert score columns to a NumPy array
    # TODO: Extract numerical score columns and convert them to a NumPy array
    # Example: scores_array = df[['Math', 'Science', 'English']].to_numpy()
    
    # Step 3: Compute average score per student using NumPy's vectorized operations
    # TODO: Compute average score per student using NumPy
    # Example: student_avg = np.mean(scores_array, axis=1)
    
    # Step 4: Add the computed average as a new column in the DataFrame
    # TODO: Add the computed average scores as a new column in the DataFrame
    
    # Step 5: Compute class average for each subject using pandas
    # TODO: Compute class averages for each subject using pandas
    # Example: math_avg = df['Math'].mean()
    
    # Step 6: (Optional) Filter students with Math scores above the class average
    # TODO: Filter students with Math scores above the class average
    # Example: top_math_students = df[df['Math'] > math_avg]


# ================================
# Main Execution for All Exercises
# ================================
def main_exercises():
    pandas_exercise()


if __name__ == '__main__':
    main_exercises()
