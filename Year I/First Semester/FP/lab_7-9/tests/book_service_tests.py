from service.book_service import BookService


class TestBookService:

    def __init__(self, service: BookService):
        self.__service = service

    def add_book_test(self):
        title = "Carte 1"
        author = "Autor 1"
        description = "Descrierea primei carti."

        assert self.__service.get_size() == 0
        self.__service.add_book(title, author, description)

        assert self.__service.get_size() == 1
        assert self.__service.get_book(0).get_id() == 100001
        assert self.__service.get_book(0).get_title() == 'Carte 1'
        assert self.__service.get_book(0).get_author() == 'Autor 1'

        try:

            self.__service.add_book('', title, description)
            assert False

        except ValueError:
            assert True

    def update_book_test(self):
        specified_book = self.__service.get_book(0)
        new_title = 'Titlu nou'
        new_author = 'Autor nou'
        new_description = None
        old_description = specified_book.get_description()
        self.__service.update_book(specified_book, new_title, new_author, new_description)

        assert self.__service.get_book(0).get_author() == new_author
        assert self.__service.get_book(0).get_title() == new_title
        assert self.__service.get_book(0).get_description() == old_description

        try:

            self.__service.update_book(specified_book, '', new_author, new_description)
            assert False

        except ValueError:
            assert True

    def search_book_test(self):
        assert self.__service.search_book(100001) is not None

        try:
            self.__service.search_book(10)
            assert False
        except ValueError:
            assert True

    def delete_book_test(self):
        specified_book = self.__service.get_book(0)

        assert self.__service.get_size() == 1
        self.__service.delete_book(specified_book)

        assert self.__service.get_size() == 0

    def run_tests(self):
        self.add_book_test()
        self.update_book_test()
        self.search_book_test()
        self.delete_book_test()
