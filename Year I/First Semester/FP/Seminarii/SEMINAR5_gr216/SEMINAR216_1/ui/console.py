from colorama import Fore, Style

from SEMINAR216_1.domain.task import to_str
from SEMINAR216_1.list_manager.task_manager import *


def print_menu():
    print('1. Adaugare task')
    print('2. Cautare task cu deadline intre 2 date')
    print('3. Stergere task dupa descriere')
    print('4. Eliminare task-uri dupa status')
    print('5. Filtrare: afisare task-uri carre contin in descriere string')
    print('6. Afisare raport pe luna')
    print('7. Undo')
    print('P. Afisarea tuturor task-urilor')
    print('A. Adaugare task-uri default')
    print('E. Iesire')


def print_task_list(task_list):
    for task in task_list:
        print(to_str(task))


def search_task_ui(task_list):
    print('Introduceti datele:')
    try:
        zi_start = int(input('Zi start:'))
        luna_start = int(input('Luna start:'))
        zi_finish = int(input('Zi finish:'))
        luna_finish = int(input('Zi finish:'))
        exista_task = search_task_by_date(task_list, zi_start, luna_start, zi_finish, luna_finish)
        if exista_task:
            print('Exista task intre datele date.')
        else:
            print('Nu exista task intre datele date.')
    except ValueError:
        print(Fore.RED + 'EROARE: Introduceti numere pentru date.' + Style.RESET_ALL)


def add_task_ui(task_manager_data):
    descriere = input("Introduceti descrierea:")
    data = input("Introduceti data:")
    status = input("Introduceti status:")
    try:
        elements_date = data.split('-')
        day = int(elements_date[0].strip())
        month = int(elements_date[1].strip())
        add_task(task_manager_data, descriere, day, month, status)
    except ValueError as e:
        print(Fore.RED + "EROARE:" + Style.RESET_ALL + str(e))


def delete_by_description_ui(task_manager_data):
    descriere = input("Introduceti descrierea dupa care se sterge:")
    try:
        delete_task_by_description(task_manager_data, descriere)
        print("Dupa stergere, lista cu task-uri este:")
        print_task_list(get_current_list(task_manager_data))
    except IndexError as e:
        print(Fore.RED + "EROARE:" + Style.RESET_ALL + str(e))


def delete_by_status_ui(task_manager_data):
    status = input("Introduceti statusul dupa care se sterge:")
    delete_by_status(task_manager_data, status)
    print("Dupa stergere, lista cu task-uri este:")
    print_task_list(get_current_list(task_manager_data))


def show_report_ui(task_list):
    report = get_report_by_day(task_list)
    # report is a dict
    for day, tasks in report.items():
        print('Ziua:', day)
        print_task_list(tasks)


def undo_ui(task_manager_data):
    try:
        undo(task_manager_data)
        print(Fore.GREEN + 'SUCCES:' + "Undo efectuat cu succes." + Style.RESET_ALL)

    except ValueError as e:
        print(Fore.RED + 'ERROR:' + str(e) + Style.RESET_ALL)


def filter_by_description_ui(task_list):
    descriere_substr = input('Introduceti parte din descriere:')
    print('Task-urile care contin in descriere textul dat sunt:')
    filtered_tasks = filter_by_description(task_list, descriere_substr)
    print_task_list(filtered_tasks)


def start():
    task_manager_data = create_task_manager()
    while True:
        print_menu()
        option = input('>')
        option = option.upper().strip()
        if option == "P":
            print_task_list(get_current_list(task_manager_data))
        elif option == "A":
            add_default_tasks(get_current_list(task_manager_data))
        elif option == '1':
            add_task_ui(task_manager_data)
        elif option == '2':
            search_task_ui(get_current_list(task_manager_data))
        elif option == '3':
            delete_by_description_ui(task_manager_data)
        elif option == '4':
            delete_by_status_ui(task_manager_data)
        elif option == '5':
            filter_by_description_ui(get_current_list(task_manager_data))
        elif option == '6':
            show_report_ui(get_current_list(task_manager_data))
        elif option == '7':
            undo_ui(task_manager_data)
        elif option == "E":
            break
        else:
            print("Invalid option.")
