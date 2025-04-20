import sqlite3

def initialize_database():
    """Создание структуры БД"""

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        bith_date TEXT,
        biography TEXT          
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT       
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        publication_year INTEGER,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id)           
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS book_genre (
        book_id INTEGER,
        genre_id INTEGER,
        PRIMARY KEY (book_id, genre_id),
        FOREIGN KEY (book_id) REFERENCES books(id),         
        FOREIGN KEY (genre_id) REFERENCES genres(id)           
    )
    """)



# Инициализация базы данных при запуске
initialize_database()