from repository.client_repo import *
from domain.client import Client


class ClientController:
    def __init__(self, validator: ClientValidator, repository: ClientInMemory):
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

    def search_for_client(self, client_info, key):
        """
        Finds a client in the list of clients
        :param client_info: the clients name or id
        :param key: the key that we search by (either 'name' or 'id')
        :type key: str
        :return:
        """
        if key == 'id':
            if client_info > 200000:
                for client in self.__repo.get_all():
                    if client.get_id() == client_info:
                        return client
            else:
                raise ValueError("ID-ul introdus nu este valid.")
        else:
            for client in self.__repo.get_all():
                if client.get_name() == client_info:
                    return client
        return None

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
        self.__repo.store(updated_client)


    def delete_client(self, specified_client):
        """
        Deletes a client
        :param specified_client: a client
        :type specified_client: Client
        :return: -
        """
        self.__repo.delete(specified_client)

    def default_clients(self):
        """
        Adds a few default clients to the list
        :return:
        """
        self.__repo.store(Client('nume1 prenume1', 5000000000001))
        self.__repo.store(Client('nume2 prenume2', 6000000000002))
        self.__repo.store(Client('nume3 prenume3', 6000000000003))
        self.__repo.store(Client('nume4 prenume4', 5000000000004))

    def get_all_clients(self):
        return self.__repo.get_all()
