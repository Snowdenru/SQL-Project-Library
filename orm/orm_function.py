# orm_functions.py
from orm.models import Session, Author, Genre, Book
from typing import List, Optional

def add_author(name: str, birth_date: Optional[str] = None, biography: Optional[str] = None):
    session = Session()
    author = Author(name=name, birth_date=birth_date, biography=biography)
    session.add(author)
    session.commit()
    session.close()

def get_authors(search_name: Optional[str] = None) -> List[Author]:
    session = Session()
    query = session.query(Author)
    
    if search_name:
        query = query.filter(Author.name.ilike(f'%{search_name}%'))
    
    authors = query.all()
    session.close()
    return authors

def add_genre(name: str, description: Optional[str] = None):
    session = Session()
    genre = Genre(name=name, description=description)
    session.add(genre)
    session.commit()
    session.close()

def add_book(title: str, author_id: int, publication_year: Optional[int] = None, genre_ids: Optional[List[int]] = None):
    session = Session()
    
    book = Book(
        title=title,
        publication_year=publication_year,
        author_id=author_id
    )
    
    if genre_ids:
        genres = session.query(Genre).filter(Genre.id.in_(genre_ids)).all()
        book.genres.extend(genres)
    
    session.add(book)
    session.commit()
    session.close()

def get_books_by_author(author_id: int) -> List[Book]:
    session = Session()
    books = session.query(Book).filter(Book.author_id == author_id).all()
    session.close()
    return books

def get_books_by_genre(genre_id: int) -> List[Book]:
    session = Session()
    genre = session.query(Genre).get(genre_id)
    books = genre.books if genre else []
    session.close()
    return books

def search_books(search_term: str) -> List[Book]:
    session = Session()
    books = session.query(Book).join(Author).filter(
        (Book.title.ilike(f'%{search_term}%')) | 
        (Author.name.ilike(f'%{search_term}%'))
    ).all()
    session.close()
    return books