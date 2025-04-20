# pip install sqlalchemy alembic
 
from sqlalchemy import create_engine, Column, Integer, String, Date, Text, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Связь многие-ко-многим для книг и жанров
book_genre = Table(
    'book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Text)
    biography = Column(Text)
    
    books = relationship("Book", back_populates="author")
    
    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    
    books = relationship("Book", secondary=book_genre, back_populates="genres")
    
    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}')>"

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary=book_genre, back_populates="books")
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"

# Инициализация базы данных
engine = create_engine('sqlite:///library_orm.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

