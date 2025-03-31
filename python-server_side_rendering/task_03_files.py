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
    

def read_json():
    with open('python-server_side_rendering/products.json', 'r', encoding='utf-8') as j_file:
        data_json = json.load(j_file)
    return data_json

def read_csv():
    list_csv = []
    
    with open('python-server_side_rendering/products.csv', newline='') as csv_file:
        csvfile = csv.DictReader(csv_file)

        for row in csvfile:
            list_csv.append(row)

    return list_csv

@app.route('/products')
def products():    
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    products = []
    error_message = None

    if source == json:
        products = read_json()
    elif source == csv:
        products = read_csv()
    else:
        error_message = "Wrong source"

    if error_message is None:
        if product_id:
            products = [product for product in products if product['id'] == product_id]
            if not products:
                error_message = "Product not found"
        
    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == ('__main__'):
    app.run(debug=True, port=5000)
