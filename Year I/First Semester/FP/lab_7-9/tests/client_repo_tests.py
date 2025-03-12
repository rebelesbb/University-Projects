from repository.client_repo import ClientInMemory
from domain.client import Client


class TestClientRepo:
    def __init__(self):
        self.__test_list = ClientInMemory()

    def test_add_client(self):
        assert self.__test_list.size() == 0

        client = Client('Nume Prenume', 5000000000071)

        self.__test_list.store(client)
        assert self.__test_list.size() == 1
        added_client = self.__test_list.get_client(0)
        assert added_client.get_id() == 200001

    def test_modify_client(self):
        specified_client = self.__test_list.get_client(0)
        new_name = 'Nume_nou Prenume_nou'
        old_cnp = specified_client.get_cnp()
        updated_client = Client(new_name, old_cnp)
        updated_client.set_id(specified_client.get_id())

        self.__test_list.modify(specified_client, updated_client)

        assert self.__test_list.get_client(0).get_name() == 'Nume_nou Prenume_nou'
        assert self.__test_list.get_client(0).get_cnp() == old_cnp
        assert self.__test_list.get_client(0).get_id() == 200001

    def test_delete_client(self):
        specified_client = self.__test_list.get_client(0)

        assert self.__test_list.size() == 1

        self.__test_list.delete(specified_client)

        assert self.__test_list.size() == 0

    def run_tests(self):
        self.test_add_client()
        self.test_modify_client()
        self.test_delete_client()
