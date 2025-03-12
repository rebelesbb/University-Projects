from colorama import Fore, Style
from repository.book_repo import *
from repository.client_repo import *
from tests.client_repo_tests import *
from tests.book_repo_tests import *
from tests.book_tests import *
from tests.client_tests import *
from service.book_service import BookController
from service.client_service import ClientController
from service.rent_service import RentController


class Console:

    def __init__(self, book_controller: BookController, client_controller: ClientController, rent_controller: RentController):
        self.__book_service = book_controller
        self.__client_service = client_controller
        self.__rent_service = rent_controller

    def __print_menu(self):
        print('Disponibile: adaugari, modificari, cautari dupa id/titlu/nume, afisari')
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
        print(Fore.RED + "Exit (E)" + Style.RESET_ALL)

    def print_book_list(self):
        print('\n')
        for index, book in enumerate(self.__book_service.get_all_books()):
            print(f'{index + 1}.' + book.__str__())
        print('\n')

    def print_client_list(self):
        print('\n')
        for index, client in enumerate(self.__client_service.get_all_clients()):
            print(f'{index + 1}.' + client.__str__())
        print('\n')

    def print_rent_list(self):
        print('\n')
        for index, rent in enumerate(self.__rent_service.get_rent_list()):
            print(f'{index + 1}.' + rent.__str__())
        print('\n')

    def add_book_ui(self):
        try:
            title = input('Introduceti titlul: ').strip()
            author = input('Introduceti autorul: ').strip()
            description = input('Introduceti descrierea: ').strip()
            self.__book_service.add_book(title, author, description)
            print(Fore.GREEN + "Cartea a fost adaugata cu succes!\n" + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def add_client_ui(self):
        try:
            name = input('Introduceti numele: ').strip()
            cnp = int(input('Introduceti CNP: ').strip())
            self.__client_service.add_client(name, cnp)
            print(Fore.GREEN + "Clientul a fost adaugat cu succes!\n" + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def modify_book_ui(self, modify_key):
        try:
            if modify_key == 'id':
                specified_info = int(input("Introduceti ID-ul: ").strip())
            else:
                specified_info = input("Introduceti titlul: ").strip()

            specified_book = self.__book_service.search_book(specified_info, modify_key)

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

    def modify_client_ui(self, modify_key):
        try:
            if modify_key == 'id':
                specified_info = int(input("Introduceti ID-ul: ").strip())
            else:
                specified_info = input("Introduceti numele: ").strip()

            specified_client = self.__client_service.search_for_client(specified_info, modify_key)

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

    def search_book_ui(self, search_key):
        try:
            if search_key == 'id':
                specifed_id = int(input("Introduceti ID-ul: ").strip())
                searched_for_book = self.__book_service.search_book(specifed_id, search_key)
            else:
                specified_title = input("Introduceti titlul: ").strip()
                searched_for_book = self.__book_service.search_book(specified_title, search_key)

            if type(searched_for_book) == Book:
                print(Fore.GREEN + "Cartea cautata a fost gasita!\n" + Style.RESET_ALL, searched_for_book)
            else:
                print(Fore.BLUE + "Cartea cautata nu a fost gasita." + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def search_client_ui(self, search_key):
        try:
            if search_key == 'id':
                specified_info = int(input("Introduceti ID-ul: ").strip())
            else:
                specified_info = input("Introduceti numele: ").strip()

            searched_for_client = self.__client_service.search_for_client(specified_info, search_key)

            if type(searched_for_client) == Client:
                print(Fore.GREEN + "Clientul cautat a fost gasit!\n" + Style.RESET_ALL, searched_for_client)
            else:
                print(Fore.BLUE + "Clientul cautat nu a fost gasit." + Style.RESET_ALL)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def delete_book_ui(self, delete_key):
        try:
            if delete_key == 'id':
                specified_info = int(input("Introduceti ID-ul: ").strip())
            else:
                specified_info = input("Introduceti titlul: ").strip()

            book_to_delete = self.__book_service.search_book(specified_info, delete_key)

            if book_to_delete is not None:
                self.__book_service.delete_book(book_to_delete)
                print(Fore.GREEN + "Cartea a fost stearsa cu succes" + Style.RESET_ALL)
            else:
                print(Fore.BLUE + "Cartea pe care doriti sa o stergeti nu exista in lista." + Style.RESET_ALL)


        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def delete_client_ui(self, delete_key):
        try:
            if delete_key == 'id':
                specified_info = int(input("Introduceti ID-ul: ").strip())
            else:
                specified_info = input("Introduceti numele: ").strip()

            client_to_delete = self.__client_service.search_for_client(specified_info, delete_key)

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
                self.__rent_service.add_rent(book_id, client_id)
            except Warning as warn:
                print(Fore.BLUE+ str(warn) + Style.RESET_ALL)


        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def return_book_ui(self):
        try:

            client_id = int(input("Introduceti ID client: "))
            book_id = int(input("Introduceti ID-ul cartii care urmeaza sa fie returnata:\n>"))
            self.__rent_service.delete_rent(book_id, client_id)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

    def __book_delete_menu(self):
        print("\nEfectuati stergere dupa:")
        print(Fore.CYAN + "ID" + Style.RESET_ALL + ' | ' + Fore.CYAN + " Titlu " + Style.RESET_ALL)
        done = False
        while not done:
            delete_key = input(">").strip().lower()
            if delete_key == 'id' or delete_key == 'titlu':
                self.delete_book_ui(delete_key)
                done = True
            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{delete_key} nu este este un criteriu valid pentru stergere.\n")

    def __client_delete_menu(self):
        print("\nEfectuati stergere dupa:")
        print(Fore.CYAN + "ID" + Style.RESET_ALL + ' | ' + Fore.CYAN + " Nume " + Style.RESET_ALL)
        done = False
        while not done:
            delete_key = input(">").strip().lower()
            if delete_key == 'id' or delete_key == 'nume':
                self.delete_client_ui(delete_key)
                done = True
            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{delete_key} nu este este un criteriu valid pentru stergere.\n")

    def __modify_book_menu(self):
        print("\nEfectuati modificare dupa:")
        print(Fore.CYAN + "ID" + Style.RESET_ALL + ' | ' + Fore.CYAN + " Titlu " + Style.RESET_ALL)
        done = False
        while not done:
            modify_key = input(">").strip().lower()
            if modify_key == 'id' or modify_key == 'titlu':
                self.modify_book_ui(modify_key)
                done = True
            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{modify_key} nu este este un criteriu valid pentru modificare.\n")

    def __modify_client_menu(self):
        print("\nEfectuati modificare dupa:")
        print(Fore.CYAN + "ID" + Style.RESET_ALL + ' | ' + Fore.CYAN + " Nume " + Style.RESET_ALL)
        done = False
        while not done:
            modify_key = input(">").strip().lower()
            if modify_key == 'id' or modify_key == 'nume':
                self.modify_client_ui(modify_key)
                done = True
            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{modify_key} nu este este un criteriu valid pentru modificare.\n")

    def __client_search_menu(self):
        print("\nEfectuati cautare dupa:")
        print(Fore.CYAN + "ID" + Style.RESET_ALL + ' | ' + Fore.CYAN + " Nume " + Style.RESET_ALL)
        done = False
        while not (done):
            search_key = input(">").strip().lower()

            if search_key == 'id' or search_key == 'nume':
                self.search_client_ui(search_key)
                done = True

            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{search_key} nu este este un criteriu valid pentru cautare.\n")

    def __book_search_menu(self):
        print("\nEfectuati cautare dupa:")
        print(Fore.CYAN + "ID" + Style.RESET_ALL + ' | ' + Fore.CYAN + " Titlu " + Style.RESET_ALL + ' | ' + \
              Fore.CYAN + " Autor " + Style.RESET_ALL)
        done = False
        while not done:
            search_key = input(">").strip().lower()

            if search_key == 'id' or search_key == 'titlu':
                self.search_book_ui(search_key)
                done = True

            elif search_key == 'autor':
                done = True

            else:
                print(
                    Fore.RED + "EROARE:" + Style.RESET_ALL + f"{search_key} nu este este un criteriu valid pentru modificare.\n")

    def __print_lists_menu(self):
        done = False
        while not (done):
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

    def start_test(self):
        client_list_test = TestClientRepo()
        client_list_test.run_tests()
        book_list_test = TestBookRepo()
        book_list_test.run_tests()
        test_book()
        test_client()

    def start_menu(self):
        self.__book_service.default_books()
        self.__client_service.default_clients()
        while True:

            self.__print_menu()
            option = input("Introduceti operatiunea pe care doriti sa o efectuati.\n>").strip().lower()

            if option == 'adaugare carte':
                self.add_book_ui()

            elif option == 'stergere carte':
                self.__book_delete_menu()

            elif option == 'modificare carte':
                self.__modify_book_menu()

            elif option == 'adaugare client':
                self.add_client_ui()

            elif option == 'stergere client':
                self.__client_delete_menu()

            elif option == 'modificare client':
                self.__modify_client_menu()

            elif option == 'cautare carte':
                self.__book_search_menu()

            elif option == 'cautare client':
                self.__client_search_menu()

            elif option == 'generare raport':
                pass

            elif option == 'afisare liste':
                self.__print_lists_menu()

            elif option == 'inchiriere carte':
                self.rent_book_ui()

            elif option == 'returnare carte':
                pass

            elif option == 'exit' or option == 'e':
                break

            else:
                print(Fore.RED + "EROARE:" + Style.RESET_ALL +
                      "Operatiunea introdusa nu este valida. Incercati din nou.")

            input('Apasati ENTER pentru a continua...\n')
