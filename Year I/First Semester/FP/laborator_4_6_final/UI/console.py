from List_manager.expenses_manager import *
from colorama import Fore, Style
from Tests.expenses_manager_tests import test_expenses_management_functions
from Tests.expense_tests import test_expense_functions

def print_menu():
    """
    Prints the menu
    :return: -
    """
    print("\nP.Afisare lista de cheltuieli")
    print("1.Adaugare cheltuiala noua")
    print("2.Actualizare cheltuiala")
    print("3.Stergere cheltuieli pentru o zi data")
    print("4.Stergere cheltuieli pentru un interval de timp")
    print("5.Stergere cheltuieli de un anumit tip")
    print("6.Tiparire cheltuieli mai mari decat o anumita suma")
    print("7.Tiparire cheltuieli efectuate inainte de o si data si mai mici decat o anumita suma")
    print("8.Tiparire cheltuieli de un anumit tip")
    print("9.Tiparire suma totala pentru un anumit tip de chelltuiala")
    print("10.Determinare zi cu suma cheltuita maxima")
    print("11.Tiparire cheltuieli ce au o anumita suma data")
    print("12.Tiparire cheltuieli sortate dupa tip")
    print("13.Eliminare cheltuieli de un anumit tip")
    print("14.Eliminare cheltuieli mai mici decat o suma data")
    print("U.Undo")
    print("E.Iesire din aplicatie")


def print_list(expenses_list):
    """
    Prints the list of expenses
    :parameter expenses_list: the list of expenses
    :type expenses_list: list
    :return: -
    """

    for index, element in enumerate(expenses_list):
        print(f'{index + 1}.Ziua: {get_day(element)}')  # we do this so that the index starts from one on the printed list
        print("  Costul:", get_cost(element))
        print("  Tipul:", get_type(element))


def print_list_ui(expenses_list):
    if len(expenses_list) > 0:
        print("Lista de cheltuieli este:")
        print_list(expenses_list)
        #print('\n')
    else:
        print(Fore.LIGHTBLUE_EX + "Lista este goala." + Style.RESET_ALL)

def read_day():
    """
    Reads a day
    :return: the day
    :rtype: int
    """
    day = int(input("Introduceti ziua: "))

    return day


def read_type():
    """
    Reads a type
    :return: the type
    :rtype:  str
    """

    type_list = ('mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele')
    print(f"Introduceti tipul. {type_list}")
    type = input('>').strip().lower()

    return type


def read_cost():
    """
    Reads a cost
    :return: the cost
    :rtype: int
    """
    cost = int(input("Introduceti costul: "))

    return cost


def add_expense_ui(expenses_manager_data: dict, current_params: list):
    try:
        day = int(get_param(current_params).strip())
        cost = int(get_param(current_params).strip())
        type = get_param(current_params).strip()

        add_expense(expenses_manager_data, create_expense(day, cost, type))
        print(Fore.CYAN + "Cheltuiala a fost adaugata in lista\n" + Style.RESET_ALL)

    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))


def update_expense_ui(expenses_manager_data, current_params):
    try:
        print_list(get_expenses_list(expenses_manager_data))
        #expense_index = int(input("Introduceti numarul cheltuielii pe care doriti sa o actualizati: ").strip())
        expense_index = int(get_param(current_params))
        print("Introduceti datele noi.")
        day = int(get_param(current_params).strip())
        cost = int(get_param(current_params).strip())
        type = get_param(current_params).strip()
        new_expense = create_expense(day, cost, type)

        update_expense(expenses_manager_data, expense_index, new_expense)
        print(Fore.CYAN + 'Cheltuiala a fost actualizata.' + Style.RESET_ALL)

    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))


def delete_for_specified_day_ui(expenses_manager_data, current_params):
    try:
        specified_day = int(current_params)
        delete_for_specified_day(expenses_manager_data, specified_day)
        print(Fore.GREEN + 'Stergere realizata cu succes.\n' + Style.RESET_ALL)
    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))


def delete_for_specified_period_ui(expenses_manager_data, current_params):
    try:
        first_day = int(get_param(current_params).strip())
        last_day = int(get_param(current_params).strip())
        delete_for_specified_period(expenses_manager_data, first_day, last_day)
        print(Fore.GREEN + 'Stergere realizata cu succes.\n' + Style.RESET_ALL)
    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))


def delete_for_specified_type_ui(expenses_manager_data, current_params):
    try:
        specified_type = current_params.strip()
        delete_for_specified_type(expenses_manager_data, specified_type)
        print(Fore.GREEN + 'Stergere realizata cu succes.\n' + Style.RESET_ALL)
    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))


def search_greater_than_cost_ui(expenses_manager_data,current_params):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_cost = int(current_params)
        searched_for_elements = search_greater_than_cost(expenses_list, specified_cost)
        if len(searched_for_elements) > 0:
            print_list(searched_for_elements)
        else:
            print(f"Nu exista cheltuieli cu costul egal cu {specified_cost}")
    except ValueError as err:
        print(Fore.RED + "EROARE"  + str(err) + '\n' + Style.RESET_ALL)

def search_before_day_smaller_than_cost_ui(expenses_manager_data, current_params):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_day = int(get_param(current_params).strip())
        specified_cost = int(get_param(current_params).strip())
        searched_for_elements = search_before_day_smaller_than_cost(expenses_list,specified_day,specified_cost)
        if len(searched_for_elements) > 0:
            print_list(searched_for_elements)
        else:
            print(f"Nu exista elemente inainte de ziua {specified_day} care sa aiba costul mai mic de {specified_cost}")
    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err))

def search_by_type_ui(expenses_manager_data):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_type = read_type()
        searched_for_elements = search_by_type(expenses_list, specified_type)
        if len(searched_for_elements) > 0 :
            print_list(searched_for_elements)
        else:
            print(f"Nu exista cheltuieli de tipul {specified_type}")
    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')


def sum_for_type_ui(expenses_manager_data):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_type = read_type()
        print(f"Costul total pentru cheltuielile de tip {specified_type} este ",
              sum_for_type(expenses_list, specified_type),'\n')
    except ValueError as err:
        print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(err) + '\n')

def day_greatest_cost_ui(expenses_manager_data):
    expenses_list = get_expenses_list(expenses_manager_data)
    if len(expenses_list) > 0:
        print("Ziua in care suma a fost cea mai mare este", day_greatest_cost(expenses_list))
    else:
        print("Lista este goala. Suma nu poate fi calculata.\n")

def expenses_by_cost_ui(expenses_manager_data):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_cost = read_cost()
        report_list = expenses_by_cost(expenses_list,specified_cost)
        if len(report_list) > 0:
            print_list(report_list)
        else:
            print(f"Nu exista cheltuieli cu costul {specified_cost}\n")
    except ValueError as err:
        print(Fore.RED + "EROARE"  + str(err) + '\n' + Style.RESET_ALL)

def sorted_by_type_ui(expenses_manager_data):
    expenses_list = get_expenses_list(expenses_manager_data)
    if len(expenses_list) > 0:
        sorted_list = sorted_by_type(expenses_list)
        print_list(sorted_list)
    else:
        print("Lista este goala.\n")

def filter_elements_by_specified_type_ui(expenses_manager_data):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_type = read_type()
        filtered_list = filter_elements_by_specified_type(expenses_list,specified_type)
        if len(filtered_list) > 0:
            print_list(filtered_list)
        else:
            print(f"Nu exista alte cheltuieli pe langa cele de tipul {specified_type}\n")
    except ValueError as err:
        print(Fore.RED + "EROARE"  + str(err) + '\n' + Style.RESET_ALL)

def filter_elements_specified_cost_ui(expenses_manager_data):
    try:
        expenses_list = get_expenses_list(expenses_manager_data)
        specified_cost = read_cost()
        filtered_list = filter_elements_specified_cost(expenses_list, specified_cost)
        if len(filtered_list):
            print_list(filtered_list)
        else:
            print(f"Nu exista alte cheltuieli pe langa cele cu costul {specified_cost}\n")
    except ValueError as err:
        print(Fore.RED + "EROARE:" + str(err) + '\n' + Style.RESET_ALL)

def undo_ui(expenses_manager_data):
    try:
        undo(expenses_manager_data)
        print(Fore.GREEN + "Undo realizat cu succes.\n" + Style.RESET_ALL)
    except ValueError as err:
        print(Fore.RED + "EROARE: " + str(err) + Style.RESET_ALL)

def multiple_operations_ui(expenses_manager_data):
    option_list = ('afisare', 'adaugare', 'actualizare')
    operations_without_params = ('afisare')
    #operation_list = input('Introduceti operatiunile pe care doriti sa le efectuati:\n>').strip()
    operation_list = "adaugare: 12,14,mancare; actualizare: 2, 14, 17, intretinere; afisare"
    tokens, params = create_tokens_and_parameters_list(operation_list)

    current_token = get_token(tokens)
    option = option_list.index(current_token)
    if current_token not in operations_without_params:
        current_params = get_param(params)




def run():
    #print_menu()
    option_list = ('afisare', 'adaugare', 'actualizare', 'stergere dupa zi', 'stergere perioada','stergere tip',
                   'cautare mai mare decat cost','cautare inainte de zi, mai mic decat cost','undo')
    operations_without_params = ('afisare','undo','iesire','e')

    #operation_list = "adaugare: 12,14,mancare; actualizare: 2, 14, 17, intretinere; afisare"


    # expenses_list = []
    expenses_list = [create_expense(3,129,'telefon'),
                     create_expense(4,215,'mancare'),
                     create_expense(9,120,'intretinere'),
                     create_expense(13,20,'mancare'),
                     create_expense(15,430,'imbracaminte'),
                     create_expense(23,1000,'altele'),
                     create_expense(30,50,'telefon')
                    ]

    test_expense_functions()
    test_expenses_management_functions()
    expenses_manager_data = create_expenses_manager()
    set_current_list(expenses_manager_data, expenses_list)

    while True:

        # Reads the option
        # option = input("\nIntroduceti optiunea dorita: ")
        print(option_list)
        operation_list = input('Introduceti operatiunile pe care doriti sa le efectuati:\n>').strip()
        tokens, params = create_tokens_and_parameters_list(operation_list)


        '''
        if option.isnumeric():
            option = int(option)
        else:
            option = option.strip().upper()
        '''
        while len(tokens):
            try:
                current_token = get_token(tokens)
                if current_token not in operations_without_params:
                    current_params = get_param(params)

                if current_token == 'afisare':
                    print_list_ui(get_expenses_list(expenses_manager_data))

                elif current_token == 'adaugare':
                    add_expense_ui(expenses_manager_data, current_params)

                elif current_token == 'actualizare':
                    update_expense_ui(expenses_manager_data, current_params)

                elif current_token == "stergere dupa zi":
                    delete_for_specified_day_ui(expenses_manager_data, current_params)

                elif current_token == "stergere perioada":
                    delete_for_specified_period_ui(expenses_manager_data, current_params)

                elif current_token == "stergere tip":
                    delete_for_specified_type_ui(expenses_manager_data, current_params)

                elif current_token == "cautare mai mare decat cost":
                    search_greater_than_cost_ui(expenses_manager_data,current_params)

                elif current_token == "cautare inainte de zi, mai mic decat cost":
                    search_before_day_smaller_than_cost_ui(expenses_manager_data,current_params)

                elif current_token == "cautare dupa tip":
                    search_by_type_ui(expenses_manager_data)

                elif current_token == "suma pentru tip":
                    sum_for_type_ui(expenses_manager_data)

                elif current_token == "zi cost maxim":
                    day_greatest_cost_ui(expenses_manager_data)

                elif current_token == "":
                    expenses_by_cost_ui(expenses_manager_data)

                elif current_token == "sortare dupa tip":
                    sorted_by_type_ui(expenses_manager_data)

                elif current_token == 'filtrare dupa tip':
                    filter_elements_by_specified_type_ui(expenses_manager_data)

                elif current_token == 'filtrare dupa cost':
                    filter_elements_specified_cost_ui(expenses_manager_data)

                elif current_token == 'undo':
                    undo_ui(expenses_manager_data)

                elif current_token == 'e' or current_token == 'iesire':
                    return None



            #else: print(Fore.RED + "Optiunea introdusa nu este valida.\n" + Style.RESET_ALL)

            except ValueError as err:
                print(Fore.RED + "EROARE" + str(err) + '\n' + Style.RESET_ALL)

            #(Fore.RED + 'EROARE: Datele introduse nu sunt valide! Incercati din nou.\n' + Style.RESET_ALL))

        #input("\nApasati ENTER pentru a continua...")



#problema 4