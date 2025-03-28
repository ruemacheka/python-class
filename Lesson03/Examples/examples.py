"""
Lesson 3 Cheatsheet: Classes, Objects, and Modules in Python
============================================================
This cheatsheet covers the core concepts of Object-Oriented Programming (OOP)
in Python along with modules and packages.
"""

# 1. Defining a Class and Creating an Object
class Car:
    """A simple class to represent a car."""
    
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable
        self.year = year    # Instance variable
    
    def display_info(self):
        """Method to display car details."""
        return f"{self.year} {self.brand} {self.model}"

# Creating an object (instance of Car)
car1 = Car("Toyota", "Camry", 2022)
print(car1.display_info())  # Output: 2022 Toyota Camry


# 2. Class Attributes vs Instance Attributes
class Student:
    school = "XYZ University"  # Class attribute (shared by all instances)
    
    def __init__(self, name, student_id):
        self.name = name  # Instance attribute
        self.student_id = student_id  # Instance attribute
    
    def get_details(self):
        return f"{self.name} ({self.student_id}), School: {Student.school}"

student1 = Student("Alice", "S12345")
print(student1.get_details())  # Output: Alice (S12345), School: XYZ University


# 3. Encapsulation (Private and Public Attributes)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (name mangling)
    
    def deposit(self, amount):
        """Method to add money to the balance."""
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        """Public method to access private attribute."""
        return self.__balance

# Creating an instance
account = BankAccount("John Doe", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # This will raise an AttributeError


# 4. Inheritance (Parent and Child Classes)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Creating instances
generic_animal = Animal("Animal")
dog = Dog("Buddy")
print(generic_animal.speak())  # Output: Some generic sound
print(dog.speak())  # Output: Woof! Woof!


# 5. Polymorphism (Method Overriding)
class Bird:
    def fly(self):
        return "Flying high!"

class Penguin(Bird):
    def fly(self):
        return "I can't fly, but I can swim!"

bird = Bird()
penguin = Penguin()
print(bird.fly())  # Output: Flying high!
print(penguin.fly())  # Output: I can't fly, but I can swim!


# 6. Modules in Python (Creating and Importing)
# Save this in a separate file named `my_module.py`
"""
def greet(name):
    return f"Hello, {name}!"
"""

# In another script, import and use the module
# import my_module
# print(my_module.greet("Alice"))  # Output: Hello, Alice!


# 7. Using Built-in Modules
import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Output: Random number between 1 and 10


# 8. Creating and Importing Packages
# A package is a directory containing multiple modules
# Example Directory Structure:
"""
mypackage/
    __init__.py
    module1.py
    module2.py
"""

# Inside `mypackage/module1.py`
"""
def add(a, b):
    return a + b
"""

# Inside another script
# from mypackage import module1
# print(module1.add(5, 3))  # Output: 8


# 9. Best Practices in OOP and Modular Programming
"""
- Use meaningful class and function names
- Follow the principle of encapsulation (use private attributes when needed)
- Keep modules small and focused on a single responsibility
- Follow DRY (Don't Repeat Yourself) principle by using reusable methods
"""

# 10. Additional Resources
"""
- Understanding OOP concepts: https://realpython.com/python3-object-oriented-programming/
- Python modules and packages: https://realpython.com/python-modules-packages/
- Examples of read and write with files: https://www.w3schools.com/python/python_file_write.asp
- Working with files in Python: https://realpython.com/read-write-files-python/
"""