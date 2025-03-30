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
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'items' not in data:
            raise KeyError("item not in data")
        
        return render_template('items.html', items=data['items']), 200
    
    except FileNotFoundError:
        return "File not found. Please ensure items.json exists.", 404
    except KeyError as e:
        return f"Error: {str(e)}", 500
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", 500

if __name__ == ('__main__'):
    app.run(debug=True, port=5000)
