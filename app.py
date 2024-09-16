from flask import Flask, g
import sqlite3
from get_db import get_db

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    cur = get_db().cursor()
    print(cur)

    return "<p>Hello, World!</p>"