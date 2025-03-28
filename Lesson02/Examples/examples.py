"""
Lesson 2: Python Advanced Data Types, Control Structures, and Algorithms
Cheat Sheet & Demos
"""

# =============================
# Lists: Mutable and Ordered
# =============================
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")  # Add an element
fruits.remove("banana")  # Remove an element
print(f"Fruits List: {fruits}")

# =============================
# Tuples: Immutable and Ordered
# =============================
coordinates = (10, 20)
print(f"Tuple Example: {coordinates}")
# coordinates[0] = 30  # Uncommenting will raise an error

# =============================
# Sets: Unordered Collection of Unique Elements
# =============================
numbers = {1, 2, 3, 3, 4, 5}  # Duplicates are automatically removed
numbers.add(6)
numbers.remove(2)
print(f"Set Example: {numbers}")

# =============================
# Dictionaries: Key-Value Mapping
# =============================
student = {"name": "Alice", "age": 25, "course": "Python"}
print(f"Student Info: {student}")
print(f"Student Name: {student['name']}")

# =============================
# Indexing and Slicing
# =============================
my_list = ["Python", "Java", "C++", "JavaScript"]
print(f"First Element: {my_list[0]}")
print(f"Last Element: {my_list[-1]}")
print(f"Subset: {my_list[1:3]}")

# =============================
# Conditional Statements
# =============================
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# =============================
# Loops: For and While
# =============================
print("For Loop Example:")
for i in range(1, 6):
    print(f"Number: {i}")

print("While Loop Example:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# =============================
# Functions: Parameters and Return Values
# =============================
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# =============================
# Local and Global Scope
# =============================
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

my_function()

# =============================
# Advanced Examples on data structures
# =============================


# Example 1: List Manipulation
# =============================
"""
Task:
1. Create a list of five numbers.
2. Append a new number to the list.
3. Remove the second element from the list.
4. Sort the list in descending order.
5. Print the final list.
"""
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.pop(1)
numbers.sort(reverse=True)
print("Final List:", numbers)


# Example 2: Tuple Operations
# =============================
"""
Task:
1. Create a tuple with five different city names.
2. Extract the first three elements as a new tuple.
3. Check if a specific city exists in the tuple.
4. Print the extracted tuple and the existence check result.
"""
cities = ("New York", "Los Angeles", "Chicago", "Houston", "Miami")
sub_cities = cities[:3]
is_present = "Chicago" in cities
print("Extracted Tuple:", sub_cities)
print("Is Chicago in tuple?:", is_present)


# Example 3: Set Operations
# =============================
"""
Task:
1. Create two sets of integers.
2. Find the union and intersection of both sets.
3. Remove an element from one of the sets.
4. Print the results.
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
set1.remove(2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Set1 after removal:", set1)


# Example 4: Dictionary Manipulation
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
del students["Charlie"]
print("Updated Students Dictionary:", students)


# Example 5: Indexing and Slicing
# =============================
"""
Task:
1. Create a string containing a sentence.
2. Extract the first five characters.
3. Extract the last three characters.
4. Extract every second character from the string.
5. Print all extracted parts.
"""
sentence = "Python programming is fun!"
first_five = sentence[:5]
last_three = sentence[-3:]
every_second = sentence[::2]
print("First Five Characters:", first_five)
print("Last Three Characters:", last_three)
print("Every Second Character:", every_second)


# Example 6: Nested Data Structures
# =============================
"""
Task:
1. Create a dictionary where each key is a student name, and the value is a list of their grades.
2. Add a new student with three grades.
3. Update one student's grades by adding a new grade.
4. Calculate and print the average grade for each student.
"""
students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [88, 76, 95],
    "Charlie": [92, 81, 77]
}
students_grades["David"] = [80, 85, 88]
students_grades["Alice"].append(100)

for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s Average Grade: {average:.2f}")



# =============================
# Pseudo-coding Example: Number Guessing Game
# =============================
"""
1. Start the game
2. Generate a random number between 1 and 100
3. Repeat until the user guesses the correct number:
   a. Ask the user to enter a guess
   b. If the guess is too high, print "Too high! Try again."
   c. If the guess is too low, print "Too low! Try again."
   d. If the guess is correct, print "Congratulations! You guessed it!" and end the game
4. End the game
"""


# =============================
# Actual Implementation: Number Guessing Game
# =============================

import random

def number_guessing_game():
    target = random.randint(1, 100)
    while True:
        guess = int(input("Enter your guess (1-100): "))
        if guess > target:
            print("Too high! Try again.")
        elif guess < target:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed it!")
            break

number_guessing_game()
