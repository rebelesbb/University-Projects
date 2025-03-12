from service.event_service import EventService
from colorama import Fore, Style

class Console:
    def __init__(self, event_service: EventService):
        self.__event_service = event_service

    def print_menu(self):
        """
        Prints the menu
        :return: -
        """
        print('Adaugare eveniment')
        print('Stergere eveniment')
        print('Modificare eveniment')
        print('Adaugare client')
        print('Stergere client')
        print('Modificare client')
        print('Cautare eveniment')
        print('Cautare client')
        print('Inscriere persoana')
        print('Afisare evenimente')
        print('Afisare clienti')
        print('Iesire(e)')

    def print_list(self, list_of_entities: list):
        """
        Prints a list of entities
        :param list_of_entities: the list of entities we want to print
        :return: -
        """
        for index, entity in enumerate(list_of_entities):
            print(f"{index + 1}.{entity}\n")

    def add_event_ui(self):
        try:
            event_description = input("Introduceti descrierea evenimentului:\n>")
            event_date = input("Introduceti data (dd-mm-yyyy):\n>")
            event_time = input("Introduceti timpul la care va avea loc evenimentul (hh-mm):\n>")
            self.__event_service.add_event(event_date, event_time, event_description)
            print("Adaugare realizata cu succes!")
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))

    def delete_event_ui(self):
        try:
            event_id = int(input("Introduceti ID-ul evenimentului pe care doriti sa il stergeti:\n>"))
            self.__event_service.delete_event(event_id)
            print("Stergere realizata cu succes!")
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))

    def modify_event_ui(self):
        try:
            event_id = int(input("Introduceti ID-ul evenimentului pe care doriti sa il modificati:\n>"))
            print("Introduceti datele noi.")
            new_description = input("Introduceti descrierea noua:\n>")
            new_date = input("Introduceti data noua:\n>")
            new_time = input("Introduceti timpul nou:\n>")
            self.__event_service.update_event(event_id, new_date, new_time, new_description)

        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))

    def find_event_ui(self):
        try:
            event_id = int(input("Introduceti ID-ul evenimentului pe care doriti sa il cautati:\n>"))
            event = self.__event_service.search_event(event_id)
            if event is not None:
                print("Evenimentul a fost gasit!\n", event)
            else:
                print("Evenimentul nu a fost gasit!")
        except ValueError as err:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))


    def start_console(self):
        self.print_menu()

        while True:
            option = input("Introduceti optiunea dorita:\n>").strip().lower()
            if option == 'adaugare eveniment':
                self.add_event_ui()

            elif option == 'stergere eveniment':
                self.delete_event_ui()

            elif option == 'modificare eveniment':
                self.modify_event_ui()

            elif option == 'adaugare client':
                pass
            elif option == 'stergere client':
                pass
            elif option == 'modificare client':
                pass
            elif option == 'cautare eveniment':
                self.find_event_ui()
            elif option == 'cautare client':
                pass
            elif option == 'inscriere client':
                pass
            elif option == 'raport':
                pass
            elif option == 'afisare evenimente':
                self.print_list(self.__event_service.get_all_events())

            elif option == 'iesire' or option =='e':
                break
            else:
                print('Optiunea invalida.')

            input()


