""" Extending Dynamic Data Display to Include SQLite in Flask """
from flask import Flask, render_template, request
import json
import csv
import sqlite3


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
                return render_template('product_display.html', products=[], message="Product not found"), 200
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

def create_database():
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT OR IGNORE INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

@app.route('/sql')
def sqlite():
    return render_template('products')

if __name__ == ('__main__'):
    create_database()
    app.run(debug=True, port=5000)
