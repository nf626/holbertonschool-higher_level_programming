""" Displaying Data from JSON or CSV Files in Flask """
from flask import Flask, render_template, request
import json
import csv


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
    with open('items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'items' in data:
        return render_template('items.html', items=data['items']), 200
    else:
        return render_template('items.html', items=data), 200

@app.route('/products')
def products():
    with open('python-server_side_rendering/products.json', 'r', encoding='utf-8') as j_file:
        data_json = json.load(j_file)

    source = request.args.get('source')    
    if source == "json":
        if 'products' in data_json:
            return render_template('product_display.html', products=data_json['products']), 200



if __name__ == ('__main__'):
    app.run(debug=True, port=5000)
