"""
Lesson 6: Interactive Data Science Exercises (NBA Dataset)
-----------------------------------------------------------
This script includes:
1. NumPy Advanced Exercises
2. Pandas DataFrame Manipulation
3. Data Cleaning & Transformation
4. Exploratory Data Analysis (EDA)
5. Custom Data Visualization Challenges (With User Input)

Dataset: NBA Player Stats (Simulated)
"""

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated NBA Player Stats dataset
data = {
    'Player': ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo', 'Nikola Jokic', 
               'Luka Doncic', 'Joel Embiid', 'James Harden', 'Jayson Tatum', 'Devin Booker'],
    'Team': ['Lakers', 'Warriors', 'Nets', 'Bucks', 'Nuggets', 
             'Mavericks', '76ers', '76ers', 'Celtics', 'Suns'],
    'Position': ['SF', 'PG', 'SF', 'PF', 'C', 
                 'PG', 'C', 'SG', 'SF', 'SG'],
    'PPG': [27.3, 29.6, 28.5, 29.9, 26.2, 30.2, 33.1, 21.3, 26.7, 27.0],
    'APG': [7.4, 6.3, 5.2, 5.9, 7.8, 8.1, 4.3, 10.5, 4.4, 4.8],
    'RPG': [7.9, 4.5, 7.4, 11.7, 13.8, 9.1, 10.6, 6.2, 8.5, 5.1]
}

df_nba = pd.DataFrame(data)

print("\n========== Interactive Data Science Exercises (NBA Dataset) ==========")
print("Dataset: NBA Player Stats (10 players, 6 features)")

# -------------------------------------
# 1. NumPy Interactive Exercises
# -------------------------------------

print("\n========== NumPy Interactive Exercises ==========")

# Ask user for a matrix size
size = int(input("Enter the size of a square matrix (e.g., 3 for 3x3): "))

# TODO: Create a matrix with random values

# TODO: Compute and display row-wise and column-wise means


# -------------------------------------
# 2. Pandas DataFrame Interactive Filtering
# -------------------------------------

print("\n========== Pandas Interactive Data Filtering ==========")

# Display first few rows of the dataset
print("\nNBA Dataset Preview:\n", df_nba)

# Ask user for a filter condition
team_filter = input("\nEnter a team name to filter (Lakers, Warriors, Nets, etc.): ").strip().title()

# TODO: Filter the dataset based on user input



# -------------------------------------
# 3. Data Cleaning & Transformation
# -------------------------------------

print("\n========== Data Cleaning & Transformation ==========")

# Ask user if they want to normalize a column
column_choice = input("\nEnter a column to normalize (PPG, APG, RPG): ").strip().upper()

# TODO: Check if the input exists and normalize the selected column


# -------------------------------------
# 4. Exploratory Data Analysis (EDA)
# -------------------------------------

print("\n========== Exploratory Data Analysis (EDA) ==========")

# Show descriptive statistics
print("\nSummary Statistics:\n", df_nba.describe())

# Ask user to compute aggregate statistics
agg_column = input("\nChoose a column for aggregate statistics (PPG, APG, RPG): ").strip().upper()

# TODO: Compute mean, median, and standard deviation for the selected column


# -------------------------------------
# 5. Custom Data Visualization Challenges
# -------------------------------------

print("\n========== Data Visualization Challenges ==========")

# Ask user which plot to display
print("\nAvailable visualizations:")
print("1. Histogram of Points Per Game (PPG)")
print("2. Scatter plot of Assists vs Points")
print("3. Box plot of Rebounds by Position")

choice = input("\nEnter a number to generate the corresponding plot: ")

# Setup the plot based on user choice
plt.figure(figsize=(6,4))
sns.set_style("whitegrid")

# TODO: Generate the selected plot based on user input
if choice == "1":
    pass

elif choice == "2":
    pass

elif choice == "3":
    pass

else:
    print("\nInvalid choice. No plot generated.")

plt.show()
