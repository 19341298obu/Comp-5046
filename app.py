# app.py - main flask app

from flask import Flask, render_template
import json

app = Flask(__name__)

# load data from json file
def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        print(f"loaded {len(data)} items from data.json")
        return data
    except:
        print("error loading data.json")
        return {}

# load data when app starts
waste_data = load_data()

# home page
@app.route('/')
def home():
    return render_template('index.html')

# about page
@app.route('/about')
def about():
    return render_template('about.html')

# category page
@app.route('/category/<name>')
def category(name):
    # get items that belong to this category
    items = [item for item, cat in waste_data.items() if cat.lower() == name.lower()]
    return render_template('category.html', category=name, items=items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
