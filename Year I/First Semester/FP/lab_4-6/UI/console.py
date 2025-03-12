from Domain.expense import get_day,get_cost,get_type, create_expense
from List_manager.expense_manager import *
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

def add_expense_ui(expenses_list):
    day = read_day()
    cost = read_cost()
    type = read_type()

    add_expense(expenses_list, create_expense(day, cost, type))



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
    expenses_manager_data = create_expenses_manager()
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

        elif option == 1
            add_expense_ui(expenses_list)
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
            filtered_list_type = filter_functions.filter_elements_by_specified_type(expenses_list,specified_type)
            print_list(filtered_list_type)

        elif option == 14:
            specified_cost = read_cost()
            filtered_list_cost = filter_functions.filter_elements_specified_cost(expenses_list, specified_cost)
            print_list(filtered_list_cost)

        elif option == 'U':
            pass
        elif option == 'E':
            break