import unittest

from repository.book_repo import *
from domain.book import Book


class TestBookRepo:

    def __init__(self):
        self.__test_list = BookInMemory()

    def store_test(self):
        assert self.__test_list.size() == 0

        self.__test_list.store(Book('Carte', 'Descriere interesanta', 'Autor'))

        added_book = self.__test_list.get_book(0)

        assert added_book.get_id() == 100001
        assert self.__test_list.size() == 1

    def modify_book_test(self):
        specified_book = self.__test_list.get_book(0)
        updated_book = Book('Carte 1', 'new cool description.', 'new author')
        updated_book.set_id(specified_book.get_id())

        self.__test_list.modify(specified_book, updated_book)

        specified_book = self.__test_list.get_book(0)
        assert specified_book.get_title() == 'Carte 1'
        assert specified_book.get_author() == 'new author'
        assert specified_book.get_description() == 'new cool description.'

    def delete_book_test(self):
        specified_book = self.__test_list.get_book(0)

        assert self.__test_list.size() == 1

        self.__test_list.delete(specified_book)

        assert self.__test_list.size() == 0

    def run_tests(self):
        self.store_test()
        self.modify_book_test()
        self. delete_book_test()

class TestBookRepoFile(unittest.TestCase):
    def setUp(self): #metoda de setup se apeleaza inainte de fiecare functie de test
        # clear_file_content() undeva in utils
        pass

    def tearDown(self): #metoda care se apeleaza dupa fiecare functie de test
        # definim functiile de test
        # numele lor trebuie sa inceapa cu "test" pentreu ca pyunit sa le identifice ca metode de test
        pass

    def test(self):
        # asseruri specifice
        a,b = 0, 0
        assert a == b
        self.assertEquals(a, b)
        # self.assertRaises(expected_exception=ValueError,'o functie sau ceva idk')
