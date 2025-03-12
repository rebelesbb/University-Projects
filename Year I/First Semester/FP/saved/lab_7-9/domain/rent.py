from colorama import Fore, Style
class Rent:

    def __init__(self, book_id, client_id):
        self.__book_id = book_id
        self.__client_id = client_id

    def get_book_id(self):
        return self.__book_id

    def get_client_id(self):
        return self.__client_id

    def __eq__(self, other):
        if self.__book_id == other.get_book_id() and self.__client_id == other.get_client_id():
            return True
        return False

    def __str__(self):
        return Fore.CYAN + "ID Carte: " + Style.RESET_ALL + str(self.__book_id) + Style.RESET_ALL + ' | ' +\
               Fore.CYAN + "ID Client: " + Style.RESET_ALL + str(self.__client_id) + Style.RESET_ALL

class RentValidator:
    def __init__(self):
        pass

    def validate_rent(self, rent: Rent):
        """
        Validates a rent
        :param rent: a rent
        :raises: ValueError
        """
        errors = []
        if 100000 > rent.get_book_id():
            errors.append(f"Nu exista o carte cu id-ul {rent.get_book_id()}")

        if 200000 > rent.get_client_id():
            errors.append(f"Nu exista un client cu  id-ul {rent.get_client_id()}")

        if len(errors):
            raise ValueError(errors)
