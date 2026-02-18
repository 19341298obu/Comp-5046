# app.py - main flask application for waste segregation guide
# handles routing and data loading for the web app

from flask import Flask, render_template
import json

# create flask app instance
app = Flask(__name__)

# load waste data from json file
# returns dict of items and their categories
def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        print(f"loaded {len(data)} items from data.json")
        return data
    except:
        print("error loading data.json")
        return {}

# load data once when app starts
waste_data = load_data()

# route: home page - shows welcome message and category links
@app.route('/')
def home():
    return render_template('index.html')

# route: about page - shows app info and purpose
@app.route('/about')
def about():
    return render_template('about.html')

# route: category page - shows items in a specific category
# name param is the category (plastic, organic, glass, metal, paper)
@app.route('/category/<name>')
def category(name):
    # filter items that match the category name
    items = [item for item, cat in waste_data.items() if cat.lower() == name.lower()]
    return render_template('category.html', category=name, items=items)

# run app on port 5001 with debug mode
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
