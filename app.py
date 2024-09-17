from flask import Flask, g
import sqlite3
from components.get_db import get_db
from components.submit_post import submit_post
from components.get_posts import get_posts

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

app.add_url_rule('/submit-post', 'submit-post', submit_post, methods=["POST"])
app.add_url_rule('/get-posts', 'get-posts', get_posts, methods=["GET"])