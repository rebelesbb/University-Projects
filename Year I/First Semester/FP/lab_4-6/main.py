import reports_functions
import search_functions
from UI import filter_functions
import delete_functions
from Domain.expense import get_day, get_cost, get_type, create_expense
import re

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
    print("E.Iesire din aplicatie\n")


def print_list(expenses_list):
    """
    Prints the list of expenses
    :parameter expenses_list: the list of expenses
    :type expenses_list: list
    :return: -
    """

    print("Lista de cheltuieli este:\n")
    for index, element in enumerate(expenses_list):
        print(f'{index + 1}.Ziua: {get_day(element)}')  # we do this so that the index starts from one on the printed list
        print("  Costul:", get_cost(element))
        print("  Tipul:", get_type(element))

    print('\n')

def read_day():
    """
    Reads a day
    :return: the day
    :rtype: int
    """
    day = int(input("Introduceti ziua: "))
    while day > 31 or day < 0:  # checks if the input is valid
        print("Ziua introdusa nu este valida.")
        day = int(input("Introduceti din nou ziua: "))

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

    while type not in type_list:  # checks if the input is valid, if the read task can be found in the task list
        print("Tipul introdus nu este valid.")
        print(f"Introduceti din nou tipul. {type_list}")
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

def read_expense():
    """
    Reads the expense
    :return: the day, the cost and the type of the expense
    :rtype: int, int, int
    """
    day = read_day()

    cost = read_cost()

    type = read_type()

    return day, cost, type

def read_time_period():
    """
    Reads the first and the last day of a time period
    :return: the first and last day of the time period
    :rtype: int, int
    """
    time_period = input("Introduceti perioada pentru care vreti sa stergeti cheltuielile:").strip()
    date = re.split("[-, ]",time_period)
    first_day = int(date[0])
    last_day = int(date[1])

    #checks if the input is valid
    while first_day < 1 or first_day > 31 or last_day < 1 or last_day > 31 or last_day < first_day :
        print("Datele introduse nu sunt valide.")
        time_period = input("Introduceti din nou perioada pentru care vreti sa stergeti cheltuielile:").strip()
        first_day, last_day = re.split("[-, ]", time_period)

    return first_day, last_day



def add_expense(expenses_list,expense):
    """
    Adds an expense to the list
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :return: -
    """
    expenses_list.append(expense)

def ask_for_index(expenses_list):
    """
        Asks for an index of an expense (counting from one,
        even if the elements' intices start from 0
        :return:
        """
    # prints the list of expenses and asks for the one the user wants to update
    print_list(expenses_list)
    expense_index = int(input("Introduceti numarul cheltuielii pe care doriti sa o modificati: "))

    # asks for the expense again if the input is invalid
    while expense_index > len(expenses_list) or expense_index < 1:
        print("Numarul introdus nu este valid.")
        expense_index = int(input("Introduceti din nou numarul cheltuielii pe care doriti sa o modificati: "))
    return expense_index
def modify_expense():
    print("Introduceti datele noi.")

    day, cost, type = read_expense()
    new_expense = create_expense(day, cost, type)

    return new_expense

def update_expense(expenses_list, expense_index, new_expense):
    """
    Updates a specified expense form the list
    :param expense_index: the index of the expense we want to modify
    :type expense_index: int
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param new_expense: the new expense
    :type new_expense: dict
    :return: the updated  list of expenses
    """
    # updates the expense
    expenses_list[expense_index - 1] = new_expense



def test_update_expense():
    test_list = [create_expense(12,13,'mancare'),create_expense(15,1245,'altele')]
    new_expense = create_expense(1,900,'imbracaminte')
    update_expense(test_list,1, new_expense)
    assert test_list[0] == new_expense
    new_expense = create_expense(23,10,'telefon')
    update_expense(test_list, 2, new_expense)
    assert test_list[1] == new_expense

def test_add_expense():
    test_list = []
    assert len(test_list) == 0
    expense = create_expense(11,13,'mancare')
    add_expense(test_list,expense)
    assert len(test_list) == 1
    assert get_day(test_list[0]) == 11

def test_create_expense():
    expense = create_expense(12,234,'mancare')
    assert get_day(expense) == 12
    assert get_cost(expense) == 234
    assert get_type(expense) == 'mancare'

def tests():
    reports_functions.test_sum_for_type()
    reports_functions.test_day_greatest_cost()

    delete_functions.test_delete_for_specified_day()
    delete_functions.test_delete_for_specified_period()
    delete_functions.test_delete_for_specified_type()

    search_functions.test_search_greater_than_cost()
    search_functions.test_search_before_day_smaller_than_cost()
    search_functions.test_search_by_type()

    filter_functions.test_filter_elements_by_specified_type()
    filter_functions.test_filter_elements_specified_cost()

    test_create_expense()
    test_add_expense()
    test_update_expense()


def run():
    #expenses_list = []
    '''
    expenses_list = [create_expense(3,129,'telefon'),
                     create_expense(4,215,'mancare'),
                     create_expense(9,120,'intretinere'),
                     create_expense(13,20,'mancare'),
                     create_expense(15,430,'imbracaminte'),
                     create_expense(23,1000,'altele'),
                     create_expense(30,50,'telefon')
                    ]
                    '''
    expenses_list = [create_expense(3, 129, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere'),
                 create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele'),
                 create_expense(30, 50, 'telefon'),
                 create_expense(12,13,'mancare')
                 ]
    print_menu()
    while True:

        # Reads the option
        option = input("Introduceti optiunea dorita: ")
        if option.isnumeric() == True:
            option = int(option)
        else:
            option = option.strip().upper()

        if option == 'P':
            print_list(expenses_list)

        elif option == 1:
            day, cost, type = read_expense()
            expense = create_expense(day, cost, type)
            add_expense(expenses_list,expense)

        elif option == 2:
            expense_index = ask_for_index(expenses_list)
            new_expense = modify_expense()
            update_expense(expenses_list, expense_index, new_expense)

        elif option == 3:
            specified_day = read_day()
            delete_functions.delete_for_specified_day(expenses_list,specified_day)

        elif option == 4:
            first_day, last_day = read_time_period()
            delete_functions.delete_for_specified_period(expenses_list,first_day,last_day)

        elif option == 5:
            specified_type = read_type()
            delete_functions.delete_for_specified_type(expenses_list,specified_type)

        elif option == 6:
            specified_cost = read_cost()
            searched_for_elements = search_functions.search_greater_than_cost(expenses_list, specified_cost)
            print_list(searched_for_elements)

        elif option == 7:
            specified_day = read_day()
            specified_cost = read_cost()
            searched_for_elements = search_functions.search_before_day_smaller_than_cost(expenses_list, specified_day, specified_cost)
            print_list(searched_for_elements)

        elif option == 8:
            specified_type = read_type()
            searched_for_elements = search_functions.search_by_type(expenses_list,specified_type)
            print_list(searched_for_elements)

        elif option == 9:
            specified_type = read_type()
            print(f'Costul total pentru {specified_type} este',
                  reports_functions.sum_for_type(expenses_list, specified_type))


        elif option == 10:
            print('Ziua in care suma a fost cea mai mare este ', reports_functions.day_greatest_cost(expenses_list))


        elif option == 11:
            pass


        elif option == 12:
            sorted_list =  reports_functions.sorted_by_type(expenses_list)
            print_list(sorted_list)

        elif option == 13:
            specified_type = read_type()
            filtered_list_type = filter_functions.filter_elements_by_specified_type(expenses_list, specified_type)
            print_list(filtered_list_type)

        elif option == 14:
            specified_cost = read_cost()
            filtered_list_cost = filter_functions.filter_elements_specified_cost(expenses_list, specified_cost)
            print_list(filtered_list_cost)

        elif option == 'U':
            pass
        elif option == 'E':
            break


tests()
run()


"""
try:

except: 
"""