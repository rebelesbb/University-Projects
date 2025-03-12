from repository.book_repo import *
from domain.book import Book

class TestBookRepo:

    def __init__(self):
        self.__test_list = BookInMemory()

    def store_test(self):
        self.__test_list.clear()
        assert self.__test_list.size() == 0

        self.__test_list.store(Book('Carte', 'Descriere interesanta', 'Autor'))

        added_book = self.__test_list.get_book(0)

        assert added_book.get_id() == 100001
        assert self.__test_list.size() == 1

    #de mutat in service

    """
    def find_book_test(self):
        test_list = BookInMemory()
        test_list.store('Carte1', 'Descriere interesanta1', 'Autor1')
        test_list.store('Carte2', 'Descriere interesanta2', 'Autor2')

        book1 = Book('Carte1', 'Descriere interesanta1', 'Autor1')
        book1.set_id(100001)
        assert test_list.search_book('Carte1', 'titlu') == book1

        assert test_list.search_book('Carte3', 'titlu') == -1

        book2 = Book('Carte2', 'Descriere interesanta2', 'Autor2')
        book2.set_id(100002)
        assert test_list.search_book(100002, 'id') == book2

        assert test_list.search_book(100003, 'id') == -1

        try:
            test_list.search_book(90, 'id')
            assert False
        except ValueError:
            assert True
    """

    def modify_book_test(self):
        self.__test_list.clear()
        specified_book = Book('Carte 1', 'Descrierea primei carti.','Autor 1')
        self.__test_list.store(specified_book)

        updated_book = Book('Carte 1', 'new cool description.', 'new author')
        updated_book.set_id(specified_book.get_id())
        assert updated_book.get_id() == self.__test_list.get_previous_book_id()

        self.__test_list.modify(specified_book, updated_book)


        specified_book = self.__test_list.get_book(0)
        assert specified_book.get_title() == 'Carte 1'
        assert specified_book.get_author() == 'new author'
        assert specified_book.get_description() == 'new cool description.'


    def run_tests(self):
        self.store_test()
        self.modify_book_test()


test = TestBookRepo()
test.run_tests()
