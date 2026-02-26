# app.py - waste segregation guide

from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        print(f"loaded {len(data)} items from data.json")
        return data
    except:
        print("error loading data.json")
        return {}

waste_data = load_data()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/category/<name>')
def category(name):
    items = [item for item, cat in waste_data.items() if cat.lower() == name.lower()]
    return render_template('category.html', category=name, items=items)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = []
    if query:
        # case-insensitive partial match
        for item, cat in waste_data.items():
            if query.lower() in item.lower():
                results.append({'item': item, 'category': cat})
    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)
