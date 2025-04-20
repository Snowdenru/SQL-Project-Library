# orm_interface.py
from orm.orm_function import *
from typing import List

def print_authors(authors: List[Author]):
    for author in authors:
        print(f"{author.id}. {author.name} - {author.birth_date or 'нет даты'} - {author.biography or 'нет биографии'}")

def print_books(books: List[Book]):
    session = Session()
    try:
        for book in books:
          book = session.merge(book)
          print(f"{book.id}. {book.title} ({book.publication_year or 'нет года'}) - {book.author.name}")
    finally:
        session.close()
        
def main():
    while True:
        print("\nБиблиотека (ORM) - Меню:")
        print("1. Добавить автора")
        print("2. Просмотреть авторов")
        print("3. Добавить жанр")
        print("4. Добавить книгу")
        print("5. Найти книги по автору")
        print("6. Найти книги по жанру")
        print("7. Поиск книг")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            name = input("Имя автора: ")
            birth_date = input("Дата рождения (опционально): ")
            biography = input("Биография (опционально): ")
            add_author(name, birth_date or None, biography or None)
            print("Автор добавлен")
            
        elif choice == "2":
            search = input("Поиск по имени (опционально): ")
            authors = get_authors(search if search else None)
            print_authors(authors)
                
        elif choice == "3":
            name = input("Название жанра: ")
            description = input("Описание (опционально): ")
            add_genre(name, description or None)
            print("Жанр добавлен")
            
        elif choice == "4":
            title = input("Название книги: ")
            author_id = int(input("ID автора: "))
            year = input("Год публикации (опционально): ")
            genres = input("ID жанров через запятую (опционально): ")
            
            genre_ids = [int(g.strip()) for g in genres.split(',')] if genres else None
            add_book(
                title, 
                author_id, 
                int(year) if year else None, 
                genre_ids
            )
            print("Книга добавлена")
            
        elif choice == "5":
            author_id = int(input("ID автора: "))
            books = get_books_by_author(author_id)
            print_books(books)
                
        elif choice == "6":
            genre_id = int(input("ID жанра: "))
            books = get_books_by_genre(genre_id)
            print_books(books)
                
        elif choice == "7":
            term = input("Поисковый запрос: ")
            books = search_books(term)
            print_books(books)
                
        elif choice == "0":
            break
            
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()