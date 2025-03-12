from repository.rent_repo import RentInMemory
from domain.rent import Rent, RentValidator

class RentController:
    def __init__(self, validator: RentValidator, repository: RentInMemory):
        self.__repo = repository
        self.__validator = validator

    def add_rent(self, book_id, client_id):
        """
        Adds a rent
        :param book_id: the id of the rented book
        :type: int
        :param client_id: the client that rents the book
        :type client_id: int
        :return: -
        """
        new_rent = Rent(book_id, client_id)
        self.__validator.validate_rent(new_rent)
        self.__repo.store(new_rent)

    def delete_rent(self, book_id, client_id):
        """
        Deletes a rent
        :param book_id: the id of the book
        :type book_id: int
        :param client_id: the id of the client thet rented the book
        :type client_id: int
        :return: -
        """
        rent_to_delete = Rent(book_id, client_id)
        self.__validator.validate_rent(rent_to_delete)
        self.__repo.delete(rent_to_delete)

    def get_rent_list(self):
        return self.__repo.get_all()