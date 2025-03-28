# Student Performance Tracker


# Example: Dictionary Manipulation
# =============================
"""
Task:
1. Create a dictionary with three key-value pairs representing student names and their grades.
2. Add a new student to the dictionary.
3. Update the grade of one existing student.
4. Remove one student from the dictionary.
5. Print the final dictionary.
"""
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["David"] = 88
students["Alice"] = 95
del students["Alice"]
print("Updated Students Dictionary:", students)

# In-class Exercise 2: Student Performance Tracker

# 1. Create a dictionary where each key is a student's name and the value is a dictionary containing:
#    - A list of subjects
#    - A list of corresponding grades

students = {
    "Alice": {
        "subjects": ["Math", "Science", "English"],
        "grades": [85, 90, 78]
    },
    "Bob": {
        "subjects": ["Math", "Science", "English"],
        "grades": [88, 76, 92]
    }
}

# 2. Add a new student with their subjects and grades.
students["Rue"] = {
    "subjects": ["Python", "Java", "C++"],
    "grades": [90, 85, 88]
}

# 3. Updating a grade
# Corrected: Access the "grades" list and update the grade for "Math" (index 0)
students["Alice"]["grades"][0] = 95

# Print the updated grades to verify
print("Updated Students Dictionary:", students)

# 4. Calculate and display each student's average grade.
def display_averages():
    for student, s in students.items():
        average_grade = sum(s["grades"]) / len(s["grades"])
        print(f"{student}'s average grade: {average_grade:.2f}")

# Example of displaying averages
display_averages()