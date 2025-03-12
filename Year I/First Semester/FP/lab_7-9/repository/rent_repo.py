from domain.rent import Rent
from domain.book import Book
from domain.client import Client
from datetime import date
from repository.client_repo import ClientInFile
from repository.book_repo import BookInFile


class RentInMemory:
    __previous_id = 400000

    def __init__(self):
        self.__rent_list = []

    def store(self, new_rent: Rent):
        """
        Adds a rent to the list
        :param new_rent: the new rent
        :return: -
        """
        for rent in self.__rent_list:
            if rent.get_book() == new_rent.get_book() and rent.get_status() is False:
                raise Warning("Cartea nu este disponibila momentan.")

        new_rent.generate_id(self.__previous_id)
        self.__previous_id += 1
        self.__rent_list.append(new_rent)

    def delete(self, rent: Rent):
        """
        Deletes a rent
        :param rent: the rent
        :return: -
        """
        self.__rent_list.remove(rent)

    def return_(self, rent: Rent):
        for element in self.__rent_list:
            if element == rent and element.get_status() is False:
                element.set_return()
                break

    def get_all(self):
        return self.__rent_list

    def get_rent(self, index):
        return self.__rent_list[index]

    def size(self):
        return len(self.__rent_list)


class RentInFile(RentInMemory):
    def __init__(self, file_name, book_repository: BookInFile, client_repository: ClientInFile):
        self.__book_repo = book_repository
        self.__client_repo = client_repository
        RentInMemory.__init__(self)
        self.__file_name = file_name
        self.better_load_from_file()

    def load_from_file(self):
        """
        Gets the date from the file
        """

        with open(self.__file_name, mode='r', encoding='utf-8') as rents_file:
            lines = rents_file.readlines()
            for index in range(0, len(lines), 3):
                line = lines[index]
                rent_info = [info.strip() for info in line.strip().split(';') if info != '']

                rent_id = rent_info[0]

                date_info = [int(info.strip()) for info in rent_info[1].split('-') if info != '']
                rent_date = date(date_info[0], date_info[1], date_info[2])

                return_date = rent_info[2]
                if return_date == 'None':
                    return_date = None
                else:
                    date_info = [int(info.strip()) for info in rent_info[2].split('-') if info != '']
                    return_date = date(date_info[0], date_info[1], date_info[2])

                status = rent_info[3]
                if status == 'returnata':
                    status = True
                else:
                    status = False

                line = lines[index + 1]
                book_info = [info.strip() for info in line.strip().split(';') if info != '']

                book_id = int(book_info[0])
                title = book_info[1]
                author = book_info[2]
                description = book_info[3]

                book = Book(title, description, author)
                book.set_id(book_id)

                line = lines[index + 2]
                client_info = [info.strip() for info in line.strip().split(';') if info != '']

                client_id = int(client_info[0])
                name = client_info[1]
                cnp = int(client_info[2])

                client = Client(name, cnp)
                client.set_id(client_id)

                rent = Rent(book, client)
                rent.set_id(rent_id)
                rent.set_rent_date(rent_date)
                rent.set_return_date(return_date)
                rent.set_status(status)

                RentInMemory.store(self, rent)

    def better_load_from_file(self):
        """
        Improved load from file
        """
        with open(self.__file_name, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                rent_info = [info.strip() for info in line.strip().split('; ') if info!='']
                rent_id = int(rent_info[0])
                rent_date_string = rent_info[1]
                date_info = [int(info.strip()) for info in rent_date_string.split('-') if info!= '']
                rent_date = date(date_info[0], date_info[1], date_info[2])

                return_date_string = rent_info[2]

                if return_date_string == 'None':
                    return_date = None
                else:
                    date_info = [int(info.strip()) for info in rent_date_string.split('-') if info != '']
                    return_date = date(date_info[0], date_info[1], date_info[2])

                status = rent_info[3]

                if status == 'returnata':
                    status = True
                else:
                    status = False

                book_id = int(rent_info[4])
                book = self.__book_repo.find(book_id)
                client_id = int(rent_info[5])
                client = self.__client_repo.find(client_id)

                rent = Rent(book, client)
                rent.set_id(rent_id)
                rent.set_rent_date(rent_date)
                rent.set_return_date(return_date)
                rent.set_status(status)

                RentInMemory.store(self, rent)


    def write_to_file(self):
        """
        Writes data o file
        """

        with open(self.__file_name, mode='w') as rents_file:
            rents = RentInMemory.get_all(self)
            rents_to_write = []
            for rent in rents:
                rent_id = str(rent.get_id())
                rent_date = str(rent.get_rent_date())

                return_date = rent.get_return_date()
                if return_date is None:
                    return_date = 'None'
                else:
                    return_date = str(return_date)

                status = rent.get_status()
                if status is True:
                    status = 'returnata'
                else:
                    status = 'inchiriata'

                rent_info = [rent_id, rent_date, return_date, status]
                rent_to_write = '; '.join(rent_info)

                book = rent.get_book()
                book_info = [str(book.get_id()), book.get_title(), book.get_author(), book.get_description()]
                book_to_write = '; '.join(book_info)

                client = rent.get_client()
                client_info = [str(client.get_id()), client.get_name(), str(client.get_cnp())]
                client_to_write = '; '.join(client_info)

                rents_to_write.append(rent_to_write)
                rents_to_write.append(book_to_write)
                rents_to_write.append(client_to_write)

            rents_file.write('\n'.join(rents_to_write))

    def better_write_to_file(self):
        with open(self.__file_name, mode='w') as file:
            rents = RentInMemory.get_all(self)
            rents_to_write = []
            for rent in rents:
                rent_id = str(rent.get_id())
                rent_date = str(rent.get_rent_date())
                return_date = rent.get_return_date()

                if return_date is None:
                    return_date = 'None'
                else:
                    return_date = str(return_date)

                status = rent.get_status()
                if status is False:
                    status = 'inchiriata'
                else:
                    status = 'returnata'

                book_id = str(rent.get_book().get_id())
                client_id = str(rent.get_client().get_id())
                rent_info = [rent_id, rent_date, return_date, status, book_id, client_id]
                rent_info = '; '.join(rent_info)

                rents_to_write.append(rent_info)

            rents_to_write = '\n'.join(rents_to_write)
            file.write(rents_to_write)


    def store(self, new_rent: Rent):
        """
        Adds a rent to the list
        :param new_rent: the new rent
        :return: -
        """
        RentInMemory.store(self, new_rent)
        self.better_write_to_file()

    def delete(self, rent: Rent):
        """
        Deletes a rent
        :param rent: the rent
        :return: -
        """
        RentInMemory.delete(self, rent)
        self.better_write_to_file()

    def return_(self, rent: Rent):
        RentInMemory.return_(self, rent)
        self.better_write_to_file()

    def get_all(self):
        return RentInMemory.get_all(self)

    def get_rent(self, index):
        return RentInMemory.get_rent(self, index)

    def size(self):
        return RentInMemory.size(self)
