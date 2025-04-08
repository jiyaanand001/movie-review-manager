import sqlite3

def connect():
    conn = sqlite3.connect("movies.db")
    return conn

def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    director TEXT,
                    genre TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY,
                    movie_id INTEGER,
                    rating INTEGER,
                    comment TEXT,
                    FOREIGN KEY(movie_id) REFERENCES movies(id))""")
    conn.commit()
    conn.close()

def add_movie(title, director, genre):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO movies (title, director, genre) VALUES (?, ?, ?)", (title, director, genre))
    conn.commit()
    conn.close()

def add_review(movie_title, rating, comment):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM movies WHERE title = ?", (movie_title,))
    movie = cur.fetchone()
    if movie:
        cur.execute("INSERT INTO reviews (movie_id, rating, comment) VALUES (?, ?, ?)", (movie[0], rating, comment))
        conn.commit()
    conn.close()

def view_movies():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    conn.close()
    return movies

def view_reviews(movie_title):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM movies WHERE title = ?", (movie_title,))
    movie = cur.fetchone()
    if movie:
        cur.execute("SELECT rating, comment FROM reviews WHERE movie_id = ?", (movie[0],))
        reviews = cur.fetchall()
        return reviews
    return []

def search_movies(keyword):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies WHERE title LIKE ? OR director LIKE ?", (f'%{keyword}%', f'%{keyword}%'))
    rows = cur.fetchall()
    conn.close()
    return rows
