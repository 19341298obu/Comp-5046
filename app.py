# app.py - waste segregation guide

from flask import Flask, render_template, request
from datetime import datetime
import json
import os

app = Flask(__name__)

FEEDBACK_FILE = "feedback.json"

def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        print(f"loaded {len(data)} items from data.json")
        return data
    except:
        print("error loading data.json")
        return []

waste_data = load_data()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/category/<name>')
def category(name):
    items = [item for item in waste_data if item['category'].lower() == name.lower()]
    return render_template('category.html', category=name, items=items)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = []
    if query:
        for item in waste_data:
            if query.lower() in item['name'].lower():
                results.append(item)
    return render_template('search.html', query=query, results=results)

@app.route('/recycling-rules')
def recycling_rules():
    return render_template('recycling_rules.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        if not name or not message:
            return render_template('feedback.html', error='Name and message are required.')
        
        feedback_list = []
        if os.path.exists(FEEDBACK_FILE):
            with open(FEEDBACK_FILE, 'r') as f:
                try:
                    feedback_list = json.load(f)
                except json.JSONDecodeError:
                    feedback_list = []
        
        feedback_list.append({
            'name': name,
            'email': email,
            'message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump(feedback_list, f, indent=2)
        
        return render_template('feedback_thanks.html', name=name)
    
    return render_template('feedback.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)
