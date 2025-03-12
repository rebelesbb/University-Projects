from service.client_service import ClientService


class TestClientService:

    def __init__(self, service: ClientService):
        self.__service = service

    def add_client_test(self):
        assert self.__service.get_size() == 0
        self.__service.add_client('Nume Prenume', 5050505000000)
        assert self.__service.get_size() == 1

        try:
            self.__service.add_client('Nume', 5050505050000)
            assert False
        except ValueError:
            assert True

        try:
            self.__service.add_client('', 5050505050505)
            assert False
        except ValueError:
            assert True

        try:
            self.__service.add_client('Nume Prenume', 9)
            assert False
        except ValueError:
            assert True

    def update_client_test(self):
        specified_client = self.__service.get_client(0)
        new_name = "Nume_nou Prenume_nou"
        new_cnp = None
        old_cnp = specified_client.get_cnp()
        self.__service.update_client(specified_client, new_name, new_cnp)

        assert self.__service.get_client(0).get_name() == new_name
        assert self.__service.get_client(0).get_cnp() == old_cnp
        assert self.__service.get_client(0).get_id() == 200001

        try:
            self.__service.update_client(specified_client, '', old_cnp)
            assert False
        except ValueError:
            assert True

    def search_client_test(self):
        assert self.__service.search_client(200001) is not None
        assert self.__service.search_client(200006) is None

        try:
            self.__service.search_client(200000)
            assert False
        except ValueError:
            assert True


    def delete_client_test(self):
        specified_client = self.__service.get_client(0)

        assert self.__service.get_size() == 1

        self.__service.delete_client(specified_client)

        assert self.__service.get_size() == 0

    def run_tests(self):
        self.add_client_test()
        self.update_client_test()
        self.search_client_test()
        self.delete_client_test()
