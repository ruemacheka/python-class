# Lesson 7: In-Class Exercises - Working with a New Dataset
# Dataset: Student Performance Data
# Objective: Practice data analysis and basic machine learning using alternative methods

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Sample Dataset (simulated student data)
data = {
    'StudentID': [101, 102, 103, 104, 105, 106, 107],
    'Hours_Studied': [5, 3, 8, 2, 7, 6, 1],
    'Attendance_Rate': [0.9, 0.6, 0.95, 0.5, 0.8, 0.85, 0.4],
    'Assignments_Completed': [10, 7, 12, 6, 11, 10, 4],
    'Passed': [1, 0, 1, 0, 1, 1, 0]  # 1 = Passed, 0 = Failed
}

# Create DataFrame
df = pd.DataFrame(data)

# --- Exercise 1: Basic Data Exploration ---
# TODO 1.1: Print the first few rows of the dataset

# TODO 1.2: Check for missing values

# TODO 1.3: Summary statistics


# --- Exercise 2: Data Visualization ---
# TODO 2.1: Create a pairplot of numerical features


# TODO 2.2: Create a heatmap of feature correlations


# --- Exercise 3: Data Preprocessing ---
# TODO 3.1: Normalize features (optional - here we use raw values)


# TODO 3.2: Train/Test Split


# --- Exercise 4: Train a Random Forest Model ---
# TODO 4.1: Initialize and train the classifier


# TODO 4.2: Make predictions and evaluate


# --- Exercise 5: Feature Importance ---
# TODO 5.1: Plot feature importance


# Challenge: Try other classifiers like KNeighborsClassifier or LogisticRegression
