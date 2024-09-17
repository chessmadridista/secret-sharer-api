from flask import request, jsonify
from .get_db import get_db

def _get_post_count():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM posts')
    count = cursor.fetchone()[0]
    conn.close()
    
    return count

def get_posts():
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', 5))
    no_of_posts = _get_post_count()

    if start >= end:
        message = "Please recheck your query parameters and try again."
        payload = {
            'message': message
        }
        status_code = 400
    elif start >= no_of_posts:
        message = "There are no more posts to display."
        payload = {
            "message": message
        }
        status_code = 204
    else:
        limit = end - start
        offset = start
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts LIMIT ? OFFSET ?', (limit, offset))
        column_names = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        posts = [dict(zip(column_names, row)) for row in rows]
        message = "The posts have been retrieved successfully."
        payload = {
            'posts': posts,
            'message': message,
        }
        status_code = 200

    return jsonify(payload), status_code