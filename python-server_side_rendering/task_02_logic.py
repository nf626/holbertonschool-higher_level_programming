""" Creating a Dynamic Template with Loops and Conditions in Flask """
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    return render_template('items.html')

if __name__ == ('__main__'):
    app.run(debug=True, port=5000)
