from repository.rent_repo import RentInMemory
from domain.book import Book
from domain.client import Client
from domain.rent import Rent
from datetime import date


class TestRentRepo:

    def __init__(self):
        self.__test_list = RentInMemory()

    def store_test(self):
        book = Book('Carte 1', 'Descrierea primei carti', 'Autor 1')
        book.generate_id(100000)
        client = Client('Nume Prenume', 5000000467382)
        client.generate_id(200000)
        rent = Rent(book, client)

        assert self.__test_list.size() == 0
        self.__test_list.store(rent)

        assert self.__test_list.size() == 1
        assert self.__test_list.get_rent(0) == rent
        assert self.__test_list.get_rent(0).get_id() == 400001
        assert self.__test_list.get_rent(0).get_rent_date() == date.today()

    def return_test(self):
        book = Book('Carte 1', 'Descrierea primei carti', 'Autor 1')
        book.generate_id(100000)
        client = Client('Nume Prenume', 5000000467382)
        client.generate_id(200000)
        rent = Rent(book, client)

        assert self.__test_list.get_rent(0).get_status() is False

        self.__test_list.return_(rent)

        assert self.__test_list.get_rent(0).get_return_date() == date.today()
        assert self.__test_list.get_rent(0).get_status() is True

    def run_tests(self):
        self.store_test()
        self.return_test()
