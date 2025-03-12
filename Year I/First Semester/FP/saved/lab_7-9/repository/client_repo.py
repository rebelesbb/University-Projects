from domain.client import *


class ClientInMemory:
    __previous_client_id = 200000

    def __init__(self):
        self.__client_list = []

    def __index__(self, client: Client) -> int:
        for index in range(len(self.__client_list)):
            if self.__client_list[index] == client:
                return index

    def get_client_list(self) -> list:
        return self.__client_list

    def get_client_from_list(self, index: int) -> Client:
        return self.__client_list[index]

    def store(self, client: Client):
        """
        Adds a new client to the list of clients
        :param client: a client
        :return: -
        """

        client.generate_id(self.__previous_client_id)
        self.__previous_client_id += 1
        self.__client_list.append(client)

    def modify(self, client: Client, updated_client: Client):
        """
        Modifies the values of the attributes of a client.
        :param client: the specified client
        :param updated_client: the updated data of the client
        :return: -
        """

        self.__client_list[self.__index__(client)] = updated_client

    def delete(self, client):
        """
        Deletes a specified client
        :param client: the specified client
        :return: -
        """
        self.__client_list.remove(client)


    def clear(self):
        self.__client_list.clear()

    def get_all(self):
        return self.__client_list

    def get_client(self, index):
        return self.__client_list[index]

    def size(self):
        return len(self.__client_list)
