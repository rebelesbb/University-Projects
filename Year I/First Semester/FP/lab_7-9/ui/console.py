from service.book_service import *
from service.client_service import *
from service.rent_service import *
from exceptions.exceptions import *


class Console:

    def __init__(self, book_controller: BookService, client_controller: ClientService, rent_controller: RentService):
        self.__book_service = book_controller
        self.__client_service = client_controller
        self.__rent_service = rent_controller

    @staticmethod
    def __print_menu():

        print(Fore.LIGHTCYAN_EX + "Adaugare carte  " + Style.RESET_ALL + ' | ' +
              Fore.LIGHTCYAN_EX + "Stergere carte  " + Style.RESET_ALL + ' | ' +
              Fore.LIGHTCYAN_EX + "Modificare carte " + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "Adaugare client " + Style.RESET_ALL + ' | ' +
              Fore.LIGHTCYAN_EX + "Stergere client " + Style.RESET_ALL + ' | ' +
              Fore.LIGHTCYAN_EX + "Modificare client " + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "Cautare client  " + Style.RESET_ALL + ' | ' +
              Fore.LIGHTCYAN_EX + "Cautare carte   " + Style.RESET_ALL + ' | ' +
              Fore.LIGHTCYAN_EX + "Generare raport " + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + "Inchiriere carte" + Style.RESET_ALL + ' | ' +
              Fore.LIGHTMAGENTA_EX + "Returnare carete" + Style.RESET_ALL + ' | ' +
              Fore.LIGHTMAGENTA_EX + "Afisare liste" + Style.RESET_ALL)
        print(Fore.GREEN + "Generare carti random" + Style.RESET_ALL)
        print(Fore.GREEN + "Generare clienti random" + Style.RESET_ALL)
        print(Fore.GREEN + "Generare inchirieri random" + Style.RESET_ALL)
        print(Fore.RED + "Exit (E)" + Style.RESET_ALL)

    def print_book_list(self):
        book_list = self.__book_service.get_all_books()
        if self.__book_service.get_size():
            print('\n')
            for index, book in enumerate(book_list):
                print(f'{index + 1}.' + book.__str__())
            print('\n')
        else:
            print(Fore.BLUE + "Lista este goala" + Style.RESET_ALL)

    def print_client_list(self):
        if self.__client_service.get_size():
            print('\n')
            for index, client in enumerate(self.__client_service.get_all_clients()):
                print(f'{index + 1}.' + client.__str__())
            print('\n')
        else:
            print(Fore.BLUE + "Lista este goala" + Style.RESET_ALL)

    def print_rent_list(self):
        if self.__rent_service.get_size():
            print('\n')
            for rent in self.__rent_service.get_rent_list():
                print(rent, '\n')
            print('\n')
        else:
            print(Fore.BLUE + "Lista este goala" + Style.RESET_ALL)

    def add_book_ui(self):
        try:
            title = input('Introduceti titlul: ').strip()
            author = input('Introduceti autorul: ').strip()
            description = input('Introduceti descrierea: ').strip()
            self.__book_service.add_book(title, author, description)
            print(Fore.GREEN + "Cartea a fost adaugata cu succes!\n" + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')
        except BookAlreadyExistsException as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def add_client_ui(self):
        try:
            name = input('Introduceti numele: ').strip()
            cnp = int(input('Introduceti CNP: ').strip())
            self.__client_service.add_client(name, cnp)
            print(Fore.GREEN + "Clientul a fost adaugat cu succes!\n" + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def modify_book_ui(self):
        try:

            specified_info = int(input("Introduceti ID-ul: ").strip())
            specified_book = self.__book_service.search_book(specified_info)

            if type(specified_book) == Book:

                print("Doriti sa modificati titlul? (da/nu)")
                response = input(">").strip().lower()
                if response == 'da':
                    new_title = input("Introduceti titlul nou:").strip()
                else:
                    new_title = None

                print("Doriti sa modificati autorul? (da/nu)")
                response = input(">").strip().lower()
                if response == 'da':
                    new_author = input("Introduceti autorul nou:").strip()
                else:
                    new_author = None

                print("Doriti sa modificati descrierea? (da/nu)")
                response = input(">").strip().lower()
                if response == 'da':
                    new_description = input("Introduceti descrierea noua:\n>").strip()
                else:
                    new_description = None

                self.__book_service.update_book(specified_book, new_title, new_author, new_description)
                print(Fore.GREEN + "Modificarea s-a realizat cu succes!" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + 'Cartea pe care doriti sa o modificati nu exista in lista.' + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def modify_client_ui(self):
        try:

            specified_info = int(input("Introduceti ID-ul: ").strip())
            specified_client = self.__client_service.search_client(specified_info)

            if type(specified_client) == Client:

                print("Doriti sa modificati numele? (da/nu)")
                response = input(">").strip().lower()
                if response == 'da':
                    new_name = input("Introduceti numele nou:").strip()
                else:
                    new_name = None

                print("Doriti sa modificati CNP-ul? (da/nu)")
                response = input(">").strip().lower()
                if response == 'da':
                    new_cnp = int(input("Introduceti CNP-ul nou:").strip())
                else:
                    new_cnp = None

                self.__client_service.update_client(specified_client, new_name, new_cnp)

                print(Fore.GREEN + "Modificarea s-a realizat cu succes!" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + 'Clientul pe care doriti sa il modificati nu exista in lista.' + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def search_book_ui(self):
        try:

            specifed_id = int(input("Introduceti ID-ul: ").strip())
            searched_for_book = self.__book_service.search_book(specifed_id)

            if type(searched_for_book) == Book:
                print(Fore.GREEN + "Cartea cautata a fost gasita!\n" + Style.RESET_ALL, searched_for_book)
            else:
                print(Fore.BLUE + "Cartea cautata nu a fost gasita." + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def search_client_ui(self):
        try:

            specified_info = int(input("Introduceti ID-ul: ").strip())
            searched_for_client = self.__client_service.search_client(specified_info)

            if type(searched_for_client) == Client:
                print(Fore.GREEN + "Clientul cautat a fost gasit!\n" + Style.RESET_ALL, searched_for_client)
            else:
                print(Fore.BLUE + "Clientul cautat nu a fost gasit." + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def delete_book_ui(self):
        try:

            specified_info = int(input("Introduceti ID-ul: ").strip())
            book_to_delete = self.__book_service.search_book(specified_info)

            if book_to_delete is not None:
                self.__book_service.delete_book(book_to_delete)
                print(Fore.GREEN + "Cartea a fost stearsa cu succes" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + "Cartea pe care doriti sa o stergeti nu exista in lista." + Style.RESET_ALL)


        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def delete_client_ui(self):
        try:
            specified_info = int(input("Introduceti ID-ul: ").strip())
            client_to_delete = self.__client_service.search_client(specified_info)

            if client_to_delete is not None:
                self.__client_service.delete_client(client_to_delete)
                print(Fore.GREEN + "Clientul a fost sters cu succes" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + "Clientul pe care doriti sa il stergeti nu exista in lista." + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def rent_book_ui(self):
        try:
            try:
                book_id = int(input("Introduceti ID-ul cartii care urmeaza sa fie inchiriata:\n>"))
                client_id = int(input("Introduceti ID client:\n>"))

                book = self.__book_service.search_book(book_id)
                client = self.__client_service.search_client(client_id)

                self.__rent_service.add_rent(book, client)

                print(Fore.GREEN + "Inchiriere efectuata." + Style.RESET_ALL)
            except Warning as warn:
                print(Fore.BLUE + str(warn) + Style.RESET_ALL)


        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def return_book_ui(self):
        try:

            client_id = int(input("Introduceti ID client: "))
            client = self.__client_service.search_client(client_id)
            book_id = int(input("Introduceti ID-ul cartii care urmeaza sa fie returnata:\n>"))
            book = self.__book_service.search_book(book_id)

            self.__rent_service.return_book(book, client)

            print(Fore.GREEN + "Returnare efectuata." + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def generate_random_client_ui(self):
        try:
            number = int(input("Introduceti numarul de clienti pe care doriti sa ii generati:\n>"))
            self.__client_service.generate_random_client(number)
            print(Fore.GREEN + "Generare efectuata." + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def generate_random_book_ui(self):
        try:
            number = int(input("Introduceti numarul de carti pe care doriti sa le generati:\n>"))
            self.__book_service.generate_random_books(number)
            print(Fore.GREEN + 'Generare efectuata.' + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def generate_random_rent_ui(self):
        try:
            try:
                number = int(input("Introduceti numarul de inchirieri pe care doriti sa le generati:\n>"))
                self.__rent_service.generate_random_rent(self.__book_service.get_all_books(),
                                                         self.__client_service.get_all_clients(), number)
                print(Fore.GREEN + 'Generare efectuata.' + Style.RESET_ALL)
            except Warning:
               pass
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def __generate_report_menu(self):
        print(Fore.CYAN + "\nCe raport doriti sa generati?" + Style.RESET_ALL)
        print("A.Cele mai inchiriate carti")
        print("B.Clienti cu carti inchiriate")
        print("C.Primii 20% dintre cei mai activi clienti")

        done = False

        while not done:

            option = input(Fore.CYAN + ">" + Style.RESET_ALL).strip().lower()

            if option == 'a':
                indices, times_rented = self.__rent_service.most_rented(self.__book_service.get_size())

                print('\n')
                if len(indices):
                    for index in indices:
                        print(self.__book_service.get_book(index))
                        print(Fore.GREEN + f"Inchiriata de {times_rented} ori." + Style.RESET_ALL + '\n')
                else:
                    print("Nu au fost inchiriate carti.\n")

                done = True

            elif option == 'b':
                print("Efectuare ordonare dupa:")
                print(Fore.CYAN + "Nume" + Style.RESET_ALL + ' | ' + Fore.CYAN + "Numar carti" + Style.RESET_ALL)
                sort_key = input('>')
                print('\n')

                sorted_list = self.__rent_service.sort_clients(sort_key)

                if len(sorted_list):
                    for element in sorted_list:
                        print(f"{element[1]} are {element[0]} carti inchiriate.")
                else:
                    print(Fore.BLUE + "Nu exista carti inchiriate in momentul de fata." + Style.RESET_ALL)

                done = True

            elif option == 'c':
                clients = self.__rent_service.best_clients()
                if len(clients):
                    for element in clients:
                        print(element['client'], '\n', f"Carti inchiriate: {element['rents']}")
                    done = True
                else:
                    print(Fore.BLUE + "Inca nu exista clienti la biblioteca." + Style.RESET_ALL)

            else:
                print(Fore.RED + "EROARE: " + Style.RESET_ALL +
                      "Optiunea introdusa nu este valida. Incercati din nou.\n")

    def __print_lists_menu(self):
        done = False
        while not done:
            print("\nAfisare lista de:")
            print(Fore.CYAN + "Carti" + Style.RESET_ALL + ' | ' +
                  Fore.CYAN + "Clienti" + Style.RESET_ALL + ' | ' +
                  Fore.CYAN + "Inchirieri" + Style.RESET_ALL)
            print_key = input('>').strip().lower()

            if print_key == 'carti':
                self.print_book_list()
                done = True

            elif print_key == 'clienti':
                self.print_client_list()
                done = True

            elif print_key == 'inchirieri':
                self.print_rent_list()
                done = True

            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{print_key} nu este o optiune valida pentru afisare.")

    def start_menu(self):

        while True:

            self.__print_menu()
            option = input("Introduceti operatiunea pe care doriti sa o efectuati.\n>").strip().lower()

            if option == 'adaugare carte':
                self.add_book_ui()

            elif option == 'stergere carte':
                self.delete_book_ui()

            elif option == 'modificare carte':
                self.modify_book_ui()

            elif option == 'adaugare client':
                self.add_client_ui()

            elif option == 'stergere client':
                self.delete_client_ui()

            elif option == 'modificare client':
                self.modify_client_ui()

            elif option == 'cautare carte':
                self.search_book_ui()

            elif option == 'cautare client':
                self.search_client_ui()

            elif option == 'generare raport':
                self.__generate_report_menu()

            elif option == 'afisare liste':
                self.__print_lists_menu()

            elif option == 'inchiriere carte':
                self.rent_book_ui()

            elif option == 'returnare carte':
                self.return_book_ui()

            elif option == 'generare clienti random':
                self.generate_random_client_ui()

            elif option == 'generare carti random':
                self.generate_random_book_ui()

            elif option == 'generare inchirieri random':
                self.generate_random_rent_ui()

            elif option == 'exit' or option == 'e':
                break

            else:
                print(Fore.RED + "EROARE:" + Style.RESET_ALL +
                      "Operatiunea introdusa nu este valida. Incercati din nou.")

            input('Apasati ENTER pentru a continua...\n')
