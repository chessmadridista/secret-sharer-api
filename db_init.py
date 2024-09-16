import sqlite3
from datetime import datetime

DATABASE = 'secrets.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            date_created TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def fetch_posts():
    # Retrieve all posts from the 'posts' table
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()

    # Close the connection
    conn.close()
    
    return posts

if __name__ == '__main__':
    create_table()

    # # Fetch and display posts
    # posts = fetch_posts()
    # for post in posts:
    #     print(post)
