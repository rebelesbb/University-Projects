from domain.book import Book
from exceptions.exceptions import *


class BookInMemory:
    __previous_book_id = 100000

    def __init__(self):
        self.__book_list = []

    def __index__(self, book: Book):
        for index in range(len(self.__book_list)):
            if self.__book_list[index] == book:
                return index

    def store(self, book: Book):
        """
        Adds a book in the list of books
        :param book: a book
        :return: -
        """

        for element in self.__book_list:
            if element == book:
                raise BookAlreadyExistsException()

        book.generate_id(self.__previous_book_id)
        self.__previous_book_id += 1
        self.__book_list.append(book)

    def find(self, book_id) -> Book | None:
        """
        Searches a book
        :param book_id: the id of the book
        :type book_id: int
        :return: the searched for book or None if not found
        """

        if book_id > 100000:
            for book in self.__book_list:
                if book.get_id() == book_id:
                    return book
        else:
            raise ValueError('ID-ul introdus nu este valid.')
        return None

    def recursive_find(self, book_id: int, index: int) -> Book | None:
        """
        Searches a book
        :param book_id: the id of the book
        :param index: variable used to iterate over the list of books
        :return: the searched for book or None if not found
        """
        if book_id <= 100000:
            raise ValueError('ID-ul introdus nu este valid.')

        if index < 0:
            return None
        else:
            if self.get_book(index).get_id() == book_id:
                return self.get_book(index)
            else:
                return self.recursive_find(book_id, index - 1)

    def modify(self, specified_book: Book, updated_book: Book):
        """
        Modifies a book from the list of books
        :param specified_book: the book we want to modify
        :param updated_book: the updated book
        :return: -
        """

        self.__book_list[self.__index__(specified_book)] = updated_book

    def delete(self, book: Book):
        """
        Deletes a specified book
        :param book: the specified book
        :return: -
        """
        self.__book_list.remove(book)

    def get_all(self):
        """
        Returns the list of books
        :rtype: list
        """
        return self.__book_list

    def get_book(self, index):
        """
        Returns a book.
        :rtype: Book
        """
        return self.__book_list[index]

    def size(self):
        """
        Returns the length of the list
        :rtype: int
        """
        return len(self.__book_list)


class BookInFile(BookInMemory):
    def __init__(self, file_name: str):
        BookInMemory.__init__(self)
        self.__file_name = file_name
        self.read_from_file()

    # sau apelare cu super()

    def read_from_file(self):
        """
        Gets all the data from the file
        """
        with open(self.__file_name, mode='r', encoding='utf-8') as books_file:
            lines = books_file.readlines()
            lines = [line.strip() for line in lines if line.strip() != '']
            for line in lines:
                book_id, title, author, description = line.split(';')
                title = title.strip()
                author = author.strip()
                description = description.strip()
                book = Book(title, description, author)
                # book.set_id(int(book_id.strip()))
                BookInMemory.store(self, book)

    def write_to_file(self):
        """
        Writes data in the file
        """
        books = BookInMemory.get_all(self)
        with open(self.__file_name, 'w') as file:
            for element in books:
                book = [str(element.get_id()), element.get_title(),
                        element.get_author(), element.get_description()]
                line = '; '.join(book)
                file.write(line + '\n')

    def store(self, book):
        """
        Adds a book in the list of books
        :param book: a book
        :return: -
        """
        '''
        book_list = self.read_from_file()
        previous_book_id = book_list[len(book_list)-1].get_id()

        for element in book_list:
            if element == book:
                raise ValueError('Cartea exista deja in lista.')

        book.generate_id(previous_book_id)
        previous_book_id += 1
        book_list.append(book)
        self.write_to_file(book_list)
        '''
        BookInMemory.store(self, book)
        self.write_to_file()

    def delete(self, book: Book):
        """
        Deletes a book
        :return: -
        """
        BookInMemory.delete(self, book)
        self.write_to_file()

    def modify(self, book: Book, updated_book: Book):
        """
        Modifies a book
        :param book: a book
        :param updated_book: the updated book
        :return:
        """
        BookInMemory.modify(self, book, updated_book)
        self.write_to_file()

    def find(self, book_id):
        """
        Searches a book
        :param book_id: the id of the book
        :type: int
        :return: the searched for book or None if not found
        """

        return BookInMemory.recursive_find(self, book_id, self.size() - 1)

    def get_all(self):
        """
        Returns the list of books
        :rtype: list
        """
        return BookInMemory.get_all(self)

    def get_book(self, index):
        """
        Returns a book.
        :rtype: Book
        """
        return BookInMemory.get_book(self, index)

    def size(self):
        """
        Returns the length of the list
        :rtype: int
        """
        return BookInMemory.size(self)
