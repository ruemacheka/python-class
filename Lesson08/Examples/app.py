# Lesson 8: Bridging Data Science and Web Applications with Python
# ---------------------------------------------------------------
# This Python script provides in-class examples that cover:
# 1. Basic Flask app
# 2. Serving data from pandas
# 3. Simple API endpoint returning JSON
# 4. Plotting data and rendering it in a web page
# 5. Form to accept user input
# 6. File upload and CSV processing
# 7. Simple ML prediction endpoint

from flask import Flask, jsonify, render_template_string, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('Agg')  # Use a non-interactive backend
import io
import base64
import os
from werkzeug.utils import secure_filename
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Sample data
data = {
    'Product': ['A', 'B', 'C'],
    'Sales': [1200, 850, 1000],
    'Region': ['North', 'South', 'West']
}
df = pd.DataFrame(data)

@app.route('/')
def home():
    return """
    <h1>Welcome to Flask + Data Science</h1>
    <p>Routes: /data, /plot, /form, /upload, /predict</p>
    """

@app.route('/data')
def show_data():
    return jsonify(df.to_dict(orient='records'))

@app.route('/plot')
def plot():
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df['Sales'], color='skyblue')
    ax.set_title('Sales by Product')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close(fig)

    html = f"""
    <html>
    <body>
        <h2>Sales Chart</h2>
        <img src='data:image/png;base64,{image_base64}'/>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f"<h2>Hello, {name}. You are {age} years old.</h2>"

    return """
    <form method="post">
        Name: <input type="text" name="name"><br>
        Age: <input type="number" name="age"><br>
        <input type="submit">
    </form>
    """

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        df_uploaded = pd.read_csv(filepath)
        return df_uploaded.head().to_html()

    return """
    <form method="post" enctype="multipart/form-data">
        Upload CSV: <input type="file" name="file">
        <input type="submit">
    </form>
    """

@app.route('/predict')
def predict():
    # Simple linear regression example
    x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([2, 4, 6, 8, 10])
    model = LinearRegression().fit(x, y)
    prediction = model.predict([[6]])
    return f"<h2>Prediction for x=6: {prediction[0]}</h2>"

if __name__ == '__main__':
    app.run(debug=True)

# -------------------
# Instructions:
# 1. Save this script as app.py
# 2. Run in terminal using: python app.py
# 3. Visit http://127.0.0.1:5000/ in your browser
# -------------------
