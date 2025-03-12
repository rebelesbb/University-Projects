from domain.client import *


class ClientInMemory:
    __previous_client_id = 200000

    def __init__(self):
        self.__client_list = []

    def __index__(self, client: Client) -> int:
        for index in range(len(self.__client_list)):
            if self.__client_list[index] == client:
                return index

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

    def find(self, client_info):
        """
        Finds a client in the list of clients
        :param client_info: the clients name or id
        :return: the client or None if not found
        """

        if client_info > 200000:
            for client in self.__client_list:
                if client.get_id() == client_info:
                    return client
        else:
            raise ValueError("ID-ul introdus nu este valid.")
        return None

    def recursive_find(self, client_id: int, index: int) -> Client | None:
        """
        Searches a client
        :param client_id: the id of the client
        :param index: variable used to iterate over the list of clients
        :return: the searched for client or None if not found
        """
        if client_id <= 200000:
            raise ValueError('ID-ul introdus nu este valid.')

        if index < 0:
            return None
        else:
            if self.get_client(index).get_id() == client_id:
                return self.get_client(index)
            else:
                return self.recursive_find(client_id, index - 1)

    def get_all(self):
        return self.__client_list

    def get_client(self, index: int) -> Client:
        return self.__client_list[index]

    def size(self):
        return len(self.__client_list)


class ClientInFile(ClientInMemory):
    def __init__(self, file_name):
        ClientInMemory.__init__(self)
        self.__file_name = file_name
        self.load_from_file()

    def load_from_file(self):
        """
        Gets the data from the file
        """
        with open(self.__file_name, mode='r', encoding='utf-8') as clients_file:
            lines = clients_file.readlines()
            for line in lines:
                line = [info.strip() for info in line.strip().split('; ') if info != '']
                name = line[1]
                cnp = int(line[2])
                client = Client(name, cnp)
                ClientInMemory.store(self, client)

    def write_to_file(self):
        """
        Writes data into the file
        """
        with open(self.__file_name, mode='w') as clients_file:
            clients = ClientInMemory.get_all(self)
            for client in clients:
                client_info = [str(client.get_id()), client.get_name(), str(client.get_cnp())]
                client_to_write = '; '.join(client_info)
                clients_file.write(client_to_write + '\n')

    def store(self, client: Client):
        """
        Adds a new client to the list of clients
        :param client: a client
        :return: -
        """
        ClientInMemory.store(self, client)
        self.write_to_file()

    def modify(self, client: Client, updated_client: Client):
        """
        Modifies the values of the attributes of a client.
        :param client: the specified client
        :param updated_client: the updated data of the client
        :return: -
        """

        ClientInMemory.modify(self, client, updated_client)
        self.write_to_file()

    def delete(self, client):
        """
        Deletes a specified client
        :param client: the specified client
        :return: -
        """
        ClientInMemory.delete(self, client)
        self.write_to_file()


    def find(self, client_info):
        """
        Finds a client in the list of clients
        :param client_info: the clients name or id
        :return:
        """
        return ClientInMemory.recursive_find(self, client_info, self.size() - 1)


    def get_all(self):
        return ClientInMemory.get_all(self)

    def get_client(self, index: int) -> Client:
        return ClientInMemory.get_client(self, index)

    def size(self):
        return ClientInMemory.size(self)
