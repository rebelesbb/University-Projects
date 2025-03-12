from domain.book import Book


class BookInMemory:
    __previous_book_id = 100000

    def __init__(self):
        self.__book_list = []

    def get_previous_book_id(self):
        return self.__previous_book_id

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
                raise ValueError('Cartea exista deja in lista.')

        book.generate_id(self.__previous_book_id)
        self.__previous_book_id += 1
        self.__book_list.append(book)


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


    def clear(self):
        self.__book_list.clear()

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
