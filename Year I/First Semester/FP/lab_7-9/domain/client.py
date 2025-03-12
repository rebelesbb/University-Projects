from colorama import Fore, Style


class Client:

    def __init__(self, name: str, cnp: int):
        self.__name = name
        self.__cnp = cnp
        self.__id = None

    def __str__(self):
        return Fore.CYAN + 'ID: ' + Style.RESET_ALL + str(self.__id) + ' | ' + \
            Fore.CYAN + 'Nume: ' + Style.RESET_ALL + self.__name + ' | ' + \
            Fore.CYAN + 'CNP: ' + Style.RESET_ALL + str(self.__cnp)

    def get_name(self):
        return self.__name

    def get_cnp(self):
        return self.__cnp

    def generate_id(self, last_generated_client_id):
        """
        This method generates the client's id automatically
        :param last_generated_client_id: the id generated for the previous client
        :return: -
        """
        self.__id = last_generated_client_id + 1

    def get_id(self):
        return self.__id

    def set_id(self, other: int):
        self.__id = other


    def __eq__(self, other):
        if self.__name == other.get_name() and self.__cnp == other.get_cnp():
            return True
        else:
            return False


class ClientValidator:

    @staticmethod
    def validate_client(specified_client: Client):
        """
        Validates the attributes of a specified client
        :param specified_client: a specified client
        :return: -
        :raises: ValueError
        """
        errors = []

        bad_cnp = False

        if specified_client.get_cnp() < 1000000000000:
            bad_cnp = True
        elif specified_client.get_cnp() // 1000000000000 != 5 and specified_client.get_cnp() // 1000000000000 != 6:
            bad_cnp = True

        if bad_cnp:
            errors.append('CNP-ul introdus nu este valid.')

        if specified_client.get_name() == '':
            errors.append('Nu ati introdus date pentru nume')
        elif ' ' not in specified_client.get_name():
            errors.append('Numele introdus nu este valid, este necesar sa introduceti atat numele cat si prenumele.')

        if len(errors):
            errors = '\n'.join(errors)
            raise ValueError(errors)
