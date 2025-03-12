from colorama import Fore, Style
class Book:

    def __init__(self, title: str, description: str, author:str):
        self.__title = title
        self.__description = description
        self.__author = author

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_author(self):
        return self.__author

    def set_title(self, other: str):
        self.__title = other

    def set_description(self, other: str):
        self.__description = other

    def set_author(self, other: str):
        self.__author = other

    def generate_id(self, last_generated_id: int):
        """
        This method generates the book's id automatically
        :param last_generated_id: the id generated for the previous book
        :return: -
        """
        self.__id = last_generated_id + 1

    def set_id(self, other: int):
        self.__id = other

    def get_id(self):
        return self.__id


    def __str__(self):
        return Fore.CYAN + 'ID: ' + Style.RESET_ALL+ str(self.__id) + ' | ' + \
               Fore.CYAN + 'Titlu: ' + Style.RESET_ALL + self.__title + ' | ' + \
               Fore.CYAN + 'Autor: ' + Style.RESET_ALL + self.__author + ' | ' + \
               Fore.MAGENTA + '\nDescriere: ' + Style.RESET_ALL + self.__description

    def __eq__(self, other):
        if self.__title != other.get_title() or self.__author != other.get_author() or \
            self.__description != other.get_description():
            return False
        return True

class BookValidator:

    def validate_book(self, specified_book: Book):
        """
        Validates the attributes of a book
        :param specified_book: the specified book
        :return: -
        :raises: ValueError
        """

        errors = []

        if specified_book.get_title() == '':
            errors.append('Nu ati introdus date pentru titlu.')

        if specified_book.get_author() == '':
            errors.append('Nu ati introdus date pentru autor.')

        if len(specified_book.get_description()) < 10:
            errors.append('Descrierea trebuie sa aiba minim 10 caractere.')

        if len(errors):
            raise ValueError(errors)




