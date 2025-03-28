# Python Cheatsheet: Basic Syntax, Variables, Data Types, Operators, Control Structures, and Functions

# ========================
# 1. Basic Syntax and Variables
# ========================

# Example 1: Defining Variables
name = "Alice"
age = 30
is_student = True
print(f"My name is {name}, I am {age} years old, and student status: {is_student}.")

# Example 2: User Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Example 3: Multiple Variable Assignment
x, y = 5, 10
print(f"x: {x}, y: {y}")

# ========================
# 2. Data Types
# ========================

# Example 1: Common Data Types
int_var = 123        # Integer
decimal_var = 3.14   # Float
string_var = "Python" # String
bool_var = False     # Boolean

# Example 2: Advanced Data Types
list_var = [1, 2, 3]                  # List
dict_var = {"key": "value"}         # Dictionary
tuple_var = (4, 5, 6)                # Tuple
set_var = {"apple", "banana", "cherry"} # Set

# Example 3: Checking Data Types
print(type(int_var))  # <class 'int'>
print(type(list_var)) # <class 'list'>

# ========================
# 3. Operators
# ========================

# Example 1: Arithmetic Operators
a, b = 15, 4
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation

# Example 2: Comparison Operators
print(a > b)  # True
print(a < b)  # False
print(a == b) # False

# Example 3: Logical Operators
print(a > 10 and b < 5)  # True
print(a > 20 or b < 5)   # True

# ========================
# 4. Control Structures
# ========================

# Example 1: If-Else Statements
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Example 2: For Loops
for i in range(1, 6):
    print(f"Iteration {i}")

# Example 3: While Loops
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

# ========================
# 5. Functions
# ========================

# Example 1: Basic Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Example 2: Function with Default Arguments
def greet_with_default(name="Guest"):
    return f"Welcome, {name}!"

print(greet_with_default())
print(greet_with_default("Bob"))

# Example 3: Factorial Function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120

# ========================
# 6. Additional Examples
# ========================

# Example 1: Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False

# Example 2: Palindrome Checker
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("python")) # False

# Example 3: Number Guessing Game
import random

number_to_guess = random.randint(1, 50)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed it!")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
    attempts -= 1

if attempts == 0:
    print(f"Sorry, the number was {number_to_guess}.")