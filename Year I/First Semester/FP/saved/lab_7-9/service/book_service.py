from repository.book_repo import *
from domain.book import *


class BookController:
    def __init__(self, validator: BookValidator, repository: BookInMemory):
        self.__validator = validator
        self.__repo = repository

    def add_book(self, title, author, description):
        """

        :param title:
        :param author:
        :param description:
        :return:
        """
        new_book = Book(title, description, author)
        self.__validator.validate_book(new_book)
        self.__repo.store(new_book)

    def update_book(self, specified_book: Book, new_title, new_author, new_description):
        """

        :param specified_book:
        :param new_title:
        :param new_author:
        :param new_description:
        :return:
        """
        if new_title is None:
            new_title = specified_book.get_title()
        if new_author is None:
            new_author = specified_book.get_author()
        if new_description is None:
            new_description = specified_book.get_description()

        updated_book = Book(new_title, new_description, new_author)
        self.__validator.validate_book(updated_book)

        updated_book.set_id(specified_book.get_id())

        self.__repo.modify(specified_book, updated_book)

    def delete_book(self, specified_book: Book):
        """

        :param specified_book:
        :return:
        """
        self.__repo.delete(specified_book)

    def search_book(self, book_info, key):
        """

        :param book_info:
        :param key:
        :return:
        """
        if key == 'id':
            if book_info > 100000:
                for book in self.__repo.get_all():
                    if book.get_id() == book_info:
                        return book
            else:
                raise ValueError('ID-ul introdus nu este valid.')
        else:
            if book_info != '':
                for book in self.__repo.get_all():
                    if book.get_title() == book_info:
                        return book
            else:
                raise ValueError('Titlul introdus nu este valid.')
        return None

    def get_all_books(self):
        return self.__repo.get_all()

    def default_books(self):
        """
        Adds a few default books in the list
        :return:
        """
        self.__repo.store(Book('Carte 1', 'Descrierea primei carti', 'Autor 1'))
        self.__repo.store(Book('Carte 2', 'Descrierea celei de a doua carte', 'Autor 2'))
        self.__repo.store(Book('Carte 3', 'Descrierea celei de a treia carte', 'Autor 3'))
