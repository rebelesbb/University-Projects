from domain.rent import Rent

class RentInMemory:

    def __init__(self):
        self.__rent_list = []

    def store(self, new_rent: Rent):
        """
        Adds a rent to the list
        :param new_rent: the new rent
        :return: -
        """
        for rent in self.__rent_list:
            if rent.get_book_id()  == new_rent.get_book_id():
                raise Warning("Cartea nu este disponibila momentan.")

        self.__rent_list.append(new_rent)

    def delete(self, rent: Rent):
        """
        Deletes a rent
        :param rent: the rent
        :return: -
        """
        self.__rent_list.remove(rent)

    def get_all(self):
        return self.__rent_list
