# erg_twitoff
flaskapp to compare twitter users

## Installation

TODO
Download the repo and navigate there from the commandline

## Setup

Setup and activate a virtual environment:
```sh 
pipenv install
pipenv shell
```

```Creating and migrating the database:

# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
```

## Usage

```sh
FLASK_APP=web_app.py flask run
```
This runs the app throught the __init__ file. 


