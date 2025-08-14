# FlaskPythonStarter

Starter template for creating a Flask Python Backend

## Create a virtual env

### windows:

`python -m venv .venv`

## Enter virtual env

bash:
`source .venv/Scripts/activate`

## install requirements.txt

`pip install -r requirements.txt`

## Starting the flask app

`flask run`

## Database setup

1. Download postgres
1. login to postgres at terminal `psql -d postgres -U admin`
1. Create db: `CREATE DATABASE bizza;`
1. `\connect bizza` then exit postgres sql
1. `flask shell`
1. `from app import db`
1. `db.create_all()` then exit flask shell `exit()`
1. Load sample data into db: `python sample_data.py`
1. Visit http://127.0.0.1:5000/users and confirm sample data is in the app
