# Lesson 8 Exercises: Web Application Basics with Flask & HTML
# ------------------------------------------------------------
# These exercises are focused on building Flask apps and using basic HTML templates.
# Ideal for students beginning to combine Python logic with front-end rendering.
# Exercise 1: Hello, User!
# Create a route `/hello/<name>` that greets the user with their name.
# Use HTML templates to render the greeting message.

from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_user(name):
    return render_template_string("""
        <h1>Hello, {{ name }}! Welcome to Flask.</h1>
    </body>
    </html>
    """, name=name)


#Exercise 2: Basic HTML Form
#Create a route `/info` with a GET method that shows a form asking for:
#- Name (text input)
#- Favorite color (text input)
#On form submission (POST), show a page that thanks the user and displays their inputs.
@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        favorite_color = request.form.get('favorite_color')
        
        # Render a thank-you page with the user's inputs
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Thank You</title>
        </head>
        <body>
            <h1>Thank You, {name}!</h1>
            <p>Your favorite color is {favorite_color}.</p>
        </body>
        </html>
        """
        return html
    else:
        # Render the form

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Info Form</title>
        </head>
        <body>
            <form method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required><br><br>
                <label for="favorite_color">Favorite Color:</label>
                <input type="text" id="favorite_color" name="favorite_color" required><br><br>
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
        """
        return html
    
"""
Exercise 3: Multiplication Table Generator
Build a form where the user inputs a number.
After submission, render a simple HTML page with a multiplication table for that number (1 to 10).
"""    

@app.route('/multiplication', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'POST':
        # Retrieve the number from the form
        number = int(request.form.get('number'))
        
        # Generate the multiplication table
        table = "<table border='1'>"
        table += "<tr><th>Multiplier</th><th>Result</th></tr>"
        for i in range(1, 11):
            table += f"<tr><td>{number} x {i}</td><td>{number * i}</td></tr>"
        table += "</table>"
        
        # Render the multiplication table
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Multiplication Table</title>
        </head>
        <body>
            <h1>Multiplication Table for {number}</h1>
            {table}
            <br>
            <a href="/multiplication">Go Back</a>
        </body>
        </html>
        """
        return html
    else:
        # Render the form
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Multiplication Table Generator</title>
        </head>
        <body>
            <h1>Enter a Number</h1>
            <form method="POST" action="/multiplication">
                <label for="number">Number:</label>
                <input type="number" id="number" name="number" required><br><br>
                <button type="submit">Generate Table</button>
            </form>
        </body>
        </html>
        """
        
        return html




#Exercise 4: List Display from Backend
#Define a list of fruits in Python. Create a route `/fruits` that passes this list to an HTML template.
#Render the list as an unordered bullet list using HTML templates.
#Use `render_template()` to load the HTML file.
@app.route('/fruits')
def fruits():
    # Define a list of fruits
    fruit_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    
    # Render the HTML template with the fruit list
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fruit List</title>
    </head>
    <body>
        <h1>List of Fruits</h1>
        <ul>
            {% for fruit in fruits %}
                <li>{{ fruit }}</li>
            {% endfor %}
        </ul>
        <a href="/fruits">Refresh</a>
    </body>
    </html>
    """
    
    return render_template_string(html, fruits=fruit_list)




#Exercise 5: Simple HTML Table of Users
#Create a route `/users` that passes a list of dictionaries like:
#[{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 35}]
#Render this data as an HTML table with columns for Name and Age.
@app.route('/users')
def users():
    # Define a list of users
    user_list = [{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 35}]
    
    # Render the HTML template with the user list
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User List</title>
    </head>
    <body>
        <h1>List of Users</h1>
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Age</th>
            </tr>
            {% for user in users %}
                <tr>
                    <td>{{ user.name }}</td>
                    <td>{{ user.age }}</td>
                </tr>
            {% endfor %}
        </table>
        <a href="/users">Refresh</a>
    </body>
    </html>
    """
    
    return render_template_string(html, users=user_list)
    


if __name__ == '__main__':
    app.run(debug=True)