import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.url_map.strict_slashes = False

app.config['TESTING'] = True

SECRET_KEY = os.environ.get("SECRET_KEY")


URL_PREFIX = '/api/v1'

app.config["DB_NAME"] = "docker"
app.config["DB_USER"] = "docker"
app.config["DB_PASSWORD"] = "docker"
# app.config["DB_HOST"] = "localhost"
app.config["DB_HOST"] = "testdb:5432"

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app.config['DB_USER']}:\
    {app.config['DB_PASSWORD']}@{app.config['DB_HOST']}\
        /{app.config['DB_NAME']}".replace(' ', '')

db = SQLAlchemy(app)
