""" Creating a Dynamic Template with Loops and Conditions in Flask """
from flask import Flask, render_template
import json


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
    with open('python-server_side_rendering/items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    try:
        if 'items' in data:
            return render_template('items.html', items=data['items']), 200
    except:
        raise KeyError("item not in data")
    
    # return render_template('items.html', items=data['items']), 200

if __name__ == ('__main__'):
    app.run(debug=True, port=5000)
