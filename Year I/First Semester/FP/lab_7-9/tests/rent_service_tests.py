from service.rent_service import RentService

from domain.rent import Rent
from domain.book import Book
from domain.client import Client
from datetime import date


class TestRentService:
    def __init__(self, service: RentService):
        self.__service = service

    def add_rent_test(self):
        book = Book('Carte 1', 'Descrierea primei carti', 'Autor 1')
        book.generate_id(100000)
        client = Client('Nume Prenume', 5000000467382)
        client.generate_id(200000)

        assert self.__service.get_size() == 0
        self.__service.add_rent(book, client)

        assert self.__service.get_size() == 1
        assert self.__service.get_rent(0) == Rent(book, client)
        assert self.__service.get_rent(0).get_id() == 400001

    def return_book_test(self):
        book = Book('Carte 1', 'Descrierea primei carti', 'Autor 1')
        book.generate_id(100000)
        client = Client('Nume Prenume', 5000000467382)
        client.generate_id(200000)

        assert self.__service.get_rent(0).get_status() is False

        self.__service.return_book(book, client)

        assert self.__service.get_rent(0).get_status() is True
        assert self.__service.get_rent(0).get_return_date() == date.today()

    def most_rented_test(self):
        previous_id = 100000
        book1 = Book('Carte 1', 'Descrierea primei carti', 'Autor 1')
        book1.generate_id(previous_id)
        previous_id += 1
        book2 = Book('Carte 2', 'Descrierea celei de a doua carte', 'Autor 2')
        book2.generate_id(previous_id)
        previous_id += 1
        book3 = Book('Carte 3', 'Descrierea celei de a doua carte', 'Autor 2')
        book3.generate_id(previous_id)
        previous_id += 1
        client = Client('Nume Prenume', 5050620773382)
        client.generate_id(200000)


        self.__service.add_rent(book1, client)
        self.__service.return_book(book1, client)

        self.__service.add_rent(book2, client)
        self.__service.return_book(book2, client)
        self.__service.add_rent(book2, client)
        self.__service.return_book(book2, client)

        self.__service.add_rent(book3, client)
        self.__service.return_book(book3, client)

        indices, times_rented = self.__service.most_rented(3)

        for rent in self.__service.get_rent_list():
            pass
        assert len(indices) == 2
        assert indices[0] == 0
        assert indices[1] == 1

        assert times_rented == 2

    def run_tests(self):
        self.add_rent_test()
        self.return_book_test()
        self.most_rented_test()
