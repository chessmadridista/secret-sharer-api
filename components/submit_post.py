from flask import request, jsonify
from .get_db import get_db
from datetime import datetime

def _validate_post(post_title, post_body):
    is_post_valid = False

    if post_title and post_body:
        is_post_valid = True

    return is_post_valid

def _save_post_to_db(title, body):
    conn = get_db()
    cursor = conn.cursor()
    date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO posts (title, body, date_created)
        VALUES (?, ?, ?)
    ''', (title, body, date_created))
    conn.commit()

def submit_post():
    post_title = request.form["post_title"]
    post_body = request.form["post_body"]
    is_post_valid = _validate_post(post_title, post_body)

    if is_post_valid:
        _save_post_to_db(post_title, post_body)
        message = "The post was created successfully."
        status_code = 201
    else:
        message = "Some of the fields are empty. Please fill them to create a new post."
        status_code = 422
    
    return jsonify({ 'message': message }), status_code
