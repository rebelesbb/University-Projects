from colorama import Fore, Style
from domain.client import Client
from domain.book import Book
import datetime


class Rent:

    def __init__(self, book: Book, client: Client):
        self.__book = book
        self.__client = client
        self.__rent_date = datetime.date.today()
        self.__return_date = None
        self.__returned = False
        self.__id = None

    def generate_id(self, previous_id):
        self.__id = previous_id + 1

    def get_book(self):
        return self.__book

    def get_client(self):
        return self.__client

    def get_id(self):
        return self.__id

    def get_rent_date(self):
        return self.__rent_date

    def get_return_date(self):
        return self.__return_date

    def get_status(self):
        return self.__returned

    def set_return(self):
        self.__return_date = datetime.date.today()
        self.__returned = True

    def set_rent_date(self, date):
        self.__rent_date = date

    def set_return_date(self, date):
        self.__return_date = date

    def set_status(self, status):
        self.__returned = status

    def set_id(self, id_):
        self.__id = id_

    def __eq__(self, other):
        if self.__book == other.get_book() and self.__client == other.get_client():
            return True
        return False

    def __str__(self):
        if self.__return_date is None:
            return_date = '-'
        else:
            return_date = self.__return_date
        if self.__returned is True:
            status = 'returnata'
        else:
            status = 'inchiriata'
        return (Fore.MAGENTA + "ID inchiriere: " + Style.RESET_ALL + str(self.__id) + ' | ' +
                Fore.CYAN + "Data inchiriere: " + Style.RESET_ALL + str(self.__rent_date) + ' | ' +
                Fore.CYAN + "Data returnare : " + Style.RESET_ALL + str(return_date) + ' | ' +
                Fore.CYAN + "Status: " + Style.RESET_ALL + str(status) + '\n' +
                self.__book.__str__() + Style.RESET_ALL + '\n' +
                self.__client.__str__() + Style.RESET_ALL)


class RentValidator:

    def __init__(self):
        pass

    @staticmethod
    def validate_rent(rent: Rent):

        errors = []

        if rent.get_book() is None:
            errors.append("Nu exista o carte cu ID-ul introdus.")

        if rent.get_client() is None:
            errors.append("Nu exista un client cu ID-ul introdus.")

        if len(errors):
            raise ValueError(errors)
