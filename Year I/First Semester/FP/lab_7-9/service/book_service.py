from repository.book_repo import *
from domain.book import *
import random
import names


class BookService:
    def __init__(self, validator: BookValidator, repository: BookInFile):
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

    def search_book(self, book_id):
        """
        Searches a book
        :param book_id: the id of the book
        :type: int
        :return: the searched for book or None if not found
        """
        return self.__repo.find(book_id)

    def get_all_books(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.size()

    def get_book(self, index):
        return self.__repo.get_book(index)

    def generate_random_books(self, number):
        if number > 0:
            titles = ["Echoes of Eternity", "Whispers in the Mist", "The Forgotten Symphony", "Shadows of Serendipity",
                      "Aurora's Embrace", "The Alchemy of Dreams", "Beyond the Horizon", "The Midnight Garden",
                      "Eternal Echoes", "The Enigma of Ember Falls", "Silent Symphony", "The Secret Gardeners",
                      "Serpents and Stardust", "Fragments of Fate", "Whispers of Winter", "The Labyrinth's Key",
                      "Songbirds at Sunset", "Crimson Horizon", "Chronicles of the Celestial Isles", "Midnight Reverie"]
            descriptions = ["Love blossoms amid wartime chaos.",
                            "Quest for lost enchanted artifacts.",
                            "A detective solves supernatural mysteries.",
                            "Parallel worlds collide, chaos ensues.",
                            "Forbidden magic disrupts peaceful realm.",
                            "Unexpected journey changes fate's course.",
                            "Family secrets unveil haunting past.",
                            "Alien encounter reshapes human civilization.",
                            "A cursed book alters destinies.",
                            "Time traveler prevents catastrophic event."]
            for times in range(number):
                title = random.choice(titles)
                author = names.get_full_name()
                description = random.choice(descriptions)
                new_book = Book(title, description, author)
                self.__repo.store(new_book)
        else:
            raise ValueError("Valoarea introdusa nu este valida, numarul nu poate fi negativ.")
