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

`python run.py`

## Config vars / secrets

There is a file config.template.py
rename this file to config.py and enter your actualy config variables/secrets.
Do not check config.py into version managment, it is also included in the .gitignores

## Database

### Initializing the database w/ models.py

`flask db init`

### Migrating initial table

`flask db migrate -m "users table"`

### Upgrading and downgrading the database

This actually creates the db from the migration files
`flask db upgrade`
The `'flask db downgrade` would be used to roll back migrations.

### The app.db file

The `flask db upgrade base` command creates the app.db database file.

## Login system

Users can register and login. The home page is protected from view until the user is logged in. When redirected to the login page, there is a link at the bottom to create a new user/register.

## Creating and Querying users in the DB:

`flask shell`
`u = User(username='john', email='john@example.com')`
`db.session.add(u)`
`db.session.commit()`

### Query all users

`query = sa.select(User)`
`users = db.session.scalars(query).all()`
`users`
