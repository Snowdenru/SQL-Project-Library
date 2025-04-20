import sqlite3


def add_author(name, bith_date, biography):

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO authors (name, bith_date, biography) 
        VALUES (?,?,?)
        """,
        (name, bith_date, biography),
    )
    conn.commit()
    conn.close()

def get_authors(search_name=None):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    if search_name:
        cursor.execute('SELECT * FROM authors WHERE name LIKE ?', (f'%{search_name}%',))
    else:
        cursor.execute('SELECT * FROM authors')
    
    authors = cursor.fetchall()
    conn.close()
    return authors


def add_genre(name, description):

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO genres (name, description) 
        VALUES (?,?)
        """,
        (name, description),
    )
    conn.commit()
    conn.close()


def add_book(title, author_id, publication_year, genre_ids):

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO books (title, publication_year, author_id) 
        VALUES (?,?,?)
        """,
        (title, publication_year, author_id) ,
    )
    
    book_id = cursor.lastrowid
    if genre_ids:
        for genre_id in genre_ids:
            cursor.execute("""
                 INSERT INTO book_genre (book_id, genre_id) 
                 VALUES (?,?)
                 """,  (book_id, genre_id))

    conn.commit()
    conn.close()


def get_books_by_author(author_id: int):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT b.id, b.title, b.publication_year, a.name 
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE b.author_id = ?
    ''', (author_id,))
    books = cursor.fetchall()
    conn.close()
    return books

def get_books_by_genre(genre_id: int):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT b.id, b.title, b.publication_year, a.name 
    FROM books b
    JOIN authors a ON b.author_id = a.id
    JOIN book_genre bg ON b.id = bg.book_id
    WHERE bg.genre_id = ?
    ''', (genre_id,))
    books = cursor.fetchall()
    conn.close()
    return books

def search_books(search_term: str):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT b.id, b.title, b.publication_year, a.name 
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE b.title LIKE ? OR a.name LIKE ?
    ''', (f'%{search_term}%', f'%{search_term}%'))
    books = cursor.fetchall()
    conn.close()
    return books
