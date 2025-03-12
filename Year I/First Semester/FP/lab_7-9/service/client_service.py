from repository.client_repo import *
from domain.client import Client
import random
import names


class ClientService:
    def __init__(self, validator: ClientValidator, repository: ClientInFile):
        self.__validator = validator
        self.__repo = repository

    def add_client(self, name, cnp):
        """
        Adds a new client to the list of clients
        :param name: the name of the new client
        :param cnp: the cnp of the new client
        :return: -
        """
        new_client = Client(name, cnp)
        self.__validator.validate_client(new_client)
        self.__repo.store(new_client)

    def update_client(self, specified_client: Client, new_name, new_cnp):
        """
        Modifies the values of the attributes of a client.
        :param specified_client: the specified client
        :param new_name: the new name
        :param new_cnp: the new cnp
        :return: -
        """
        if new_name is None:
            new_name = specified_client.get_name()
        if new_cnp is None:
            new_cnp = specified_client.get_cnp()

        updated_client = Client(new_name, new_cnp)
        updated_client.set_id(specified_client.get_id())
        self.__validator.validate_client(updated_client)
        self.__repo.modify(specified_client, updated_client)


    def delete_client(self, specified_client):
        """
        Deletes a client
        :param specified_client: a client
        :type specified_client: Client
        :return: -
        """
        self.__repo.delete(specified_client)


    def search_client(self, client_id):
        """
        Searches for a client
        :param client_id: the id
        :type: int
        :return: the searched client or None if nou found
        """
        return self.__repo.find(client_id)


    def generate_random_client(self, number):
        if number > 0:
            for times in range(number):
                name = names.get_full_name()
                cnp = random.randint(5000000000000, 6999999999999)
                new_client = Client(name, cnp)
                self.__repo.store(new_client)
        else:
            raise ValueError("Valoarea introdusa nu este valida, numarul nu poate fi negativ.")


    def get_all_clients(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.size()

    def get_client(self, index):
        return self.__repo.get_client(index)
