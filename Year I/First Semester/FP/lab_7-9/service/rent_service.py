from repository.rent_repo import *
from domain.rent import Rent, RentValidator
from domain.client import Client
from domain.book import Book
from random import choice
from math import inf


class RentService:
    def __init__(self, validator: RentValidator, repository: RentInFile):
        self.__repo = repository
        self.__validator = validator

    def add_rent(self, book: Book, client: Client):
        """
        Adds a rent
        :param book:the book
        :param client: the client
        :return: -
        """
        new_rent = Rent(book, client)
        self.__validator.validate_rent(new_rent)
        self.__repo.store(new_rent)

    def return_book(self, book: Book, client: Client):
        """
        Marks the return of a book
        :param book: the book
        :param client: the client
        :return: -
        """
        rent = Rent(book, client)
        self.__repo.return_(rent)

    def most_rented(self, book_list_len):
        rent_id_list = []  # check how many times each book has been rented (frequency)

        for times in range(book_list_len):
            rent_id_list.append(0)

        for rent in self.__repo.get_all():
            rent_id_list[rent.get_book().get_id() - 100001] += 1

        rented_most_times = -inf
        most_rented_book_index = []
        for index, times_rented in enumerate(rent_id_list):
            if times_rented > rented_most_times:
                most_rented_book_index.clear()
                rented_most_times = times_rented
                most_rented_book_index.append(index)

            elif times_rented == rented_most_times:
                most_rented_book_index.append(index)

        return most_rented_book_index, rented_most_times

    def sort_clients(self, sort_key):
        """

        :param sort_key:
        :return:
        """
        active_clients = []
        number_of_rents = []

        for rent in self.__repo.get_all():
            if rent.get_client() not in active_clients and rent.get_status() is False:
                active_clients.append(rent.get_client())
                number_of_rents.append(1)
            elif rent.get_client() in active_clients:
                number_of_rents[active_clients.index(rent.get_client())] += 1

        list_of_clients = []
        for number, client in zip(number_of_rents, active_clients):
            list_of_clients.append((number, client))

        if sort_key == 'nume':
            return sorted(list_of_clients, key=lambda x: x[1].get_name())
        else:
            return sorted(list_of_clients, key=lambda x: x[0], reverse=True)

    def best_clients(self):
        clients_list = []
        clients_rents = []
        for rent in self.__repo.get_all():
            if rent.get_client() not in clients_list:
                clients_list.append(rent.get_client())
                clients_rents.append(1)
            else:
                index = clients_list.index(rent.get_client())
                clients_rents[index] += 1

        clients = []
        for index in range(len(clients_list)):
            client = clients_list[index]
            pair = {'client': client, 'rents': clients_rents[index]}
            clients.append(pair)

        # clients = sorted(clients, key=lambda x: x['rents'], reverse=True)
        # clients = self.bubble_sort(clients, True, lambda x: x['rents'])
        clients = self.gnome_sort(clients, True, lambda x: x['rents'])
        twenty_perc = int(0.2 * len(clients))
        if twenty_perc < 1:
            twenty_perc = 1

        clients = clients[:twenty_perc]

        return clients

    def generate_random_rent(self, book_list, client_list, number):
        if len(book_list) and len(client_list):
            if number > 0:
                for times in range(number):
                    book = choice(book_list)
                    client = choice(client_list)
                    new_rent = Rent(book, client)
                    self.__repo.store(new_rent)
                    self.__repo.return_(new_rent)

            else:
                raise ValueError("Valoarea introdusa nu este valida, numarul trebuie sa fie mai mare decat zero.")

        else:
            raise ValueError(
                "Trebuie sa existe atat clienti cat si carti introduse inainte de generarea inchirierilor.")

    def get_rent_list(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.size()

    def get_rent(self, index):
        return self.__repo.get_rent(index)

    @staticmethod
    def bubble_sort(lst: list, reverse: bool, key=None) -> list:
        """
        Sorts a list of objects based on the given key
        :param lst: the list of objects
        :param key: the key
        :param reverse: if reverse is True, the list will be sorted in descending order
        :return: the sorted list
        """

        list_to_sort = lst
        sorted = False
        while not sorted:
            sorted = True
            for index in range(len(list_to_sort) - 1):
                if key(list_to_sort[index]) > key(list_to_sort[index + 1]):
                    aux = list_to_sort[index]
                    list_to_sort[index] = list_to_sort[index + 1]
                    list_to_sort[index + 1] = aux
                    sorted = False

        if reverse is True:
            list_to_sort.reverse()

        return list_to_sort

    @staticmethod
    def gnome_sort(lst: list, reverse: bool, key=None) -> list:
        """
        Sorts a list of objects based on the given key
        :param lst: the list of objects
        :param key: the key
        :param reverse: if reverse is True, the list will be sorted in descending order
        :return: the sorted list
        """

        list_to_sort = lst
        index = 0
        while index < len(list_to_sort):
            if index == 0:
                index = index + 1
            if key(lst[index]) >= key(lst[index - 1]):
                index = index + 1
            else:
                lst[index], lst[index - 1] = lst[index - 1], lst[index]
                index = index - 1

        if reverse is True:
            list_to_sort.reverse()

        return list_to_sort
