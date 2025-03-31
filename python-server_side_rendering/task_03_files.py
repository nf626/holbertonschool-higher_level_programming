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
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Json
    with open('products.json', 'r', encoding='utf-8') as j_file:
        data_json = json.load(j_file)

    # CSV
    csv_list = []
    with open('products.csv', 'r', encoding='utf-8', newline='') as c_file:
        csv_data = csv.DictReader(c_file)

        for row in csv_data:
            csv_list.append(row)

    if source == "json":
        if product_id:
            json_filter = [x for x in data_json if x['id'] == product_id]
            if not json_filter:
                return render_template('product_display.html', products=[]), 200
            else:
                return render_template('product_display.html', products=json_filter), 200

        else:
            if 'products' in data_json:
                return render_template('product_display.html', products=data_json['products']), 200
            else:
                return render_template('product_display.html', products=data_json), 200
    
    elif source == "csv":
        if csv_list:
            return render_template('product_display.html', products=csv_list), 200
        else:
            return "empty"
    else:
        return "Wrong source"


if __name__ == ('__main__'):
    app.run(debug=True, port=5000)
