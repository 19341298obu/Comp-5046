# Waste Segregation Guide

A web app to help students and young workers sort household waste correctly.

**Live Demo:** https://comp-5046.onrender.com

## Features

- 5 waste categories: Plastic, Organic, Glass, Metal, Paper
- 23 common household items
- Clean, mobile-friendly design
- Supports UN SDG Goal 12: Responsible Consumption and Production

## Tech Stack

- Python / Flask
- HTML / CSS
- JSON data storage
- Deployed on Render

## Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with category links |
| `/about` | About the app and its purpose |
| `/category/<name>` | Items in a category (plastic, organic, glass, metal, paper) |

## Local Development

```bash
# clone repo
git clone https://github.com/19341298obu/Comp-5046.git
cd Comp-5046

# create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run locally
python app.py
```

App runs at: http://127.0.0.1:5001/

## Project Structure

```
├── app.py              # Flask application
├── data.json           # Waste items data
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
├── static/
│   └── style.css       # Styling
└── templates/
    ├── index.html      # Home page
    ├── about.html      # About page
    └── category.html   # Category page
```

## License

COMP5046 University Project
