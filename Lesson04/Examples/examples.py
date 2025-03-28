"""
🐍 Python Cheatsheet: Lessons 1 - 3 + Hangman Essentials
======================================================
"""

# 📌 Lesson 1: Python Basics

## 🔹 Variables & Data Types
x = 10  # Integer
y = 3.14  # Float
name = "Python"  # String
is_fun = True  # Boolean

## 🔹 Operators
sum_value = 5 + 3  # Addition
diff_value = 10 - 2  # Subtraction
mult_value = 4 * 2  # Multiplication
div_value = 8 / 2  # Division
mod_value = 10 % 3  # Modulus

## 🔹 Control Structures
### Conditional Statements
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is exactly 5")
else:
    print("x is less than 5")

### Loops
for i in range(5):
    print(i)  # Prints 0 to 4

while x > 0:
    print(x)
    x -= 1

# 📌 Lesson 2: Advanced Data Types & Algorithms

## 🔹 Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add element
fruits.remove("banana")  # Remove element
print(fruits[0])  # Access element

## 🔹 Tuples (Immutable)
coordinates = (10, 20)
x, y = coordinates  # Tuple unpacking

## 🔹 Sets (Unique Elements)
numbers = {1, 2, 3, 4, 4}  # Removes duplicate 4
distinct_numbers = set([1, 1, 2, 3])

## 🔹 Dictionaries (Key-Value Pairs)
student = {"name": "Alice", "age": 22}
print(student["name"])  # Access value
student["grade"] = "A"  # Add new key-value pair

## 🔹 Functions

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 📌 Lesson 3: Functions & Problem-Solving

## 🔹 Function Parameters & Return Values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8

## 🔹 Scope (Local vs Global)
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(global_var)

my_function()
# print(local_var)  # This will cause an error (undefined)

## 🔹 Algorithm Complexity (Big O Notation)
# Example of O(n) complexity:
def print_items(lst):
    for item in lst:
        print(item)

print_items([1, 2, 3])

# 📌 Lesson 4: Hangman Game Essentials

import random

## 🔹 Choosing a Word Randomly
def choose_word():
    words = ["python", "developer", "hangman", "programming"]
    return random.choice(words)

## 🔹 Displaying the Word with Guessed Letters
def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

## 🔹 Getting User Input
def get_guess():
    while True:
        guess = input("Enter a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        print("Invalid input. Please enter a single letter.")

## 🔹 Checking Win Condition
def check_win_condition(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

