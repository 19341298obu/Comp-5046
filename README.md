# Comp 5046 Project

Waste classification web app.

## Setup

```bash
cd comp5046-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

App runs at: http://127.0.0.1:5001/

## Routes

- `/` - Home page
- `/about` - About page
- `/category/<name>` - Category page (e.g. /category/plastic)

## Data

Waste items stored in `data.json` in project root.
