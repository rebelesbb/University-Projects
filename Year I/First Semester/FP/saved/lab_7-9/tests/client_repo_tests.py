from repository.client_repo import ClientInMemory
from domain.client import Client

class TestClientRepo:
    def __init__(self):
        self.__test_list = ClientInMemory()

    def test_add_client(self):
        self.__test_list.clear()

        assert self.__test_list.size() == 0

        client = Client('Nume Prenume', 5000000000071)

        self.__test_list.store(client)
        assert self.__test_list.size() == 1
        added_client = self.__test_list.get_client(0)
        assert added_client.get_id() == 200001


    # de mutat in service
    '''
    def test_find_client(self):
        test_list = ClientInMemory()
        test_list.default_clients()

        searched_for_client = Client('nume2 prenume2', 6000000000002)
        searched_for_client.set_id(200002)
        assert test_list.search_for_client(200002, 'id') == searched_for_client

        assert test_list.search_for_client('nume2 prenume2', 'nume') == searched_for_client

        assert test_list.search_for_client('nume10 prenume10', 'nume') == -1
        assert test_list.search_for_client(200010, 'id') == -1


        try:
            test_list.search_for_client(10, 'id')
            assert False
        except:
            assert True
    '''

    def test_modify_client(self):
        test_list = ClientInMemory()
        test_list.default_clients()

        specified_client = test_list.search_for_client(200001, 'id')
        test_list.modify(specified_client, 'Nume Nou', None)

        updated_client = test_list.search_for_client(200001, 'id')
        assert updated_client.get_name() == 'Nume Nou'
        assert updated_client.get_cnp() == specified_client.get_cnp()


    def run_tests(self):
        self.test_add_client()
        self.test_find_client()
        self.test_modify_client()

