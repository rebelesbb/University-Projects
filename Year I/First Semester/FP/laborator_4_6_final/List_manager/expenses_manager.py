from Domain.expense import *
from math import inf
from Utils.expense_utils import copy_expense
from Utils.list_utils import copy_list_expenses


def create_expenses_manager() -> dict:
    """

    :return:
    """
    undo_list = []
    expenses_list = []
    return {'undo_list': undo_list, 'expenses_list': expenses_list}


def get_undo_list(expenses_manager_data: dict):
    return expenses_manager_data['undo_list']


def get_expenses_list(expenses_manager_data: dict):
    return expenses_manager_data['expenses_list']


def set_current_list(expenses_manager_data: dict, new_list):
    expenses_manager_data['expenses_list'] = new_list


def set_element_current_list(expenses_list, expense, index):
    expenses_list[index] = expense

def set_undo_list(expenses_manager_data: dict, previous_state_list:list):
    expenses_manager_data['undo_list'].append(previous_state_list)


def add_expense(expenses_manager_data, expense):
    """
    Adds an expense to the list
    :param expenses_manager_data: the necessary data for the expenses management
    :type expenses_manager_data: dict
    :return: -
    """
    validate_expense(expense)

    expenses_list = get_expenses_list(expenses_manager_data)
    set_undo_list(expenses_manager_data,copy_list_expenses(expenses_list))
    expenses_list.append(expense)


def update_expense(expenses_manager_data: dict, expense_index, new_expense):
    """
    Updates a specified expense form the list
    :param expense_index: the index of the expense we want to modify
    :type expense_index: int
    :param expenses_manager_data: the necessary data for expenses management (expenses list, undo list)
    :type expenses_manager_data: dict
    :param new_expense: the new expense
    :type new_expense: dict
    :return: the updated  list of expenses
    """
    # updates the expense
    if 0 < expense_index <= len(get_expenses_list(expenses_manager_data)):
        validate_expense(new_expense)
        set_undo_list(expenses_manager_data, copy_list_expenses(get_expenses_list(expenses_manager_data)))
        set_element_current_list(get_expenses_list(expenses_manager_data), new_expense, expense_index - 1)
    else:
        raise ValueError(f"Nu exista o cheltuiala cu numarul {expense_index}")


def delete_for_specified_day(expenses_manager_data: dict, specified_day):
    """
    Deletes all the expenses for a specified day
    :param expenses_manager_data: the necessary data for expenses management (expenses list, undo list)
    :type expenses_manager_data: dict
    :param specified_day: the specified day
    :type specified_day: int
    :return: -
    """
    if 0 < specified_day < 32:
        set_undo_list(expenses_manager_data, copy_list_expenses(get_expenses_list(expenses_manager_data)))
        expenses_list = get_expenses_list(expenses_manager_data)
        for index in reversed(range(len(expenses_list))):
            if get_day(expenses_list[index]) == specified_day:
                del expenses_list[index]
    else:
        raise ValueError("Ziua introdusa nu este valida")


def delete_for_specified_period(expenses_manager_data, first_day, last_day):
    """
    Deletes all expenses for a specified period of the time
    :param expenses_manager_data: the necessary data for expenses management (expenses list, undo list)
    :type expenses_manager_data: dict
    :param first_day: the first day of the time period
    :type first_day: int
    :param last_day: the last day of the time period
    :type last_day: int
    :return: -
    """
    if 0 < first_day < 32 and 0 < last_day < 32 and first_day < last_day:
        set_undo_list(expenses_manager_data, copy_list_expenses(get_expenses_list(expenses_manager_data)))
        expenses_list = get_expenses_list(expenses_manager_data)
        for index in reversed(range(len(expenses_list))):
            if first_day <= get_day(expenses_list[index]) <= last_day:
                del expenses_list[index]
    else:
        raise ValueError("Datele introduse nu sunt valide.")


def delete_for_specified_type(expenses_manager_data, specified_type):
    """
    Deletes all expenses for a specified type
    :param expenses_manager_data: the necessary data for expenses management (expenses list, undo list)
    :type expenses_manager_data: dict
    :param specified_type: the specified type
    :type specified_type: str
    :return: -
    """
    type_list = ('mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele')
    if specified_type in type_list:
        set_undo_list(expenses_manager_data, copy_list_expenses(get_expenses_list(expenses_manager_data)))
        expenses_list = get_expenses_list(expenses_manager_data)
        for index in reversed(range(len(expenses_list))):
            if get_type(expenses_list[index]) == specified_type:
                del expenses_list[index]
    else:
        raise ValueError("Tipul introdus nu este valid.")


def search_greater_than_cost(expenses_list, specified_cost):
    """
    Searches and creates a list of all expenses that have a greater cost than the specified one
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_cost: the specified cost
    :type specified_cost: int
    :return: the list of the expenses we searched for
    :rtype: list
    """
    new_list = []
    for element in expenses_list:
        if get_cost(element) > specified_cost:
            new_list.append(element)
    return new_list


def search_before_day_smaller_than_cost(expenses_list, specified_day, specified_cost):
    """
    Searches and creates a list of all the expenses that were made before the specified day
    and have a smaller cost than the specified one
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_day: the specified day
    :type specified_day: int
    :param specified_cost: the specified cost
    :type specified_cost: int
    :return: the list of the expenses we searched for
    :rtype: list
    """

    if 0 < specified_day < 32:
        new_list = []

        for element in expenses_list:
            if get_day(element) < specified_day and get_cost(element) < specified_cost:
                new_list.append(element)

        return new_list

    else:
        raise ValueError("Ziua introdusa nu este valida")


def search_by_type(expenses_list, specified_type):
    """
    Searches and creates a list of all the expenses that have the specified type
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_type: the specified type
    :type specified_type: str
    :return: the list of the expenses we searched for
    :rtype: list
    """
    type_list = ('mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele')
    if specified_type in type_list:
        new_list = []

        for element in expenses_list:
            if get_type(element) == specified_type:
                new_list.append(element)

        return new_list
    else:
        raise ValueError("Tipul introdus nu este valid.")


def sum_for_type(expenses_list, specified_type):
    """
    Calculates the sum of all expenses of a specified type
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_type: the specified type
    :type specified_type: str
    :return: the sum
    :rtype: int
    """
    type_list = ('mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele')
    if specified_type in type_list:
        Sum = 0
        for element in expenses_list:
            if get_type(element) == specified_type:
                Sum += get_cost(element)
        return Sum
    else:
        raise ValueError("Tipul introdus nu este valid.")

def day_greatest_cost(expenses_list):
    """
    Determines the day of the expense with the greatest cost
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :return: the day of the expense with the greatest cost
    :rtype: int
    """
    the_day = -1  # this variable represents the day of the expense with the greatest cost
    greatest_cost = -inf

    for element in expenses_list:
        if get_cost(element) > greatest_cost:
            greatest_cost = get_cost(element)
            the_day = get_day(element)

    return the_day

def expenses_by_cost(expenses_list, specified_cost):
    """
    Creates a new list of all expenses that have the specified cost
    for it to be later printed
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_cost: the specified cost
    :type specified_cost: int
    :return: the list of expenses that have the specified cost
    :rtype: list
    """
    report_list = []  # the list we use for the report, that will contain only the expenses that have the specified cost
    for element in expenses_list:
        if get_cost(element) == specified_cost:
            report_list.append(element)

    return report_list

def sorted_by_type(expenses_list):
    """
    Sorts the list by type
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :return: the sorted list
    :rtype: list
    """
    # sorted_list = sorted(expenses_list, key= lambda element: get_type(element))
    sorted_list = copy_list_expenses(expenses_list)

    # sorts the elements in the list by type
    for first_index in range(len(sorted_list) - 1):
        for second_index in range(first_index + 1, len(sorted_list)):
            if get_type(sorted_list[first_index]) > get_type(sorted_list[second_index]):
                aux = copy_expense(sorted_list[first_index])
                sorted_list[first_index] = sorted_list[second_index]
                sorted_list[second_index] = aux

    return sorted_list

def filter_elements_by_specified_type(expenses_list, specified_type):
    """
    Filters the list, eliminating all the expenses with a specified type
    without modifying the actual list
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_type: the specified type
    :type specified_type: str
    :return: the filtered list
    :rtype: list
    """

    return [element for element in expenses_list if get_type(element) != specified_type]


def filter_elements_specified_cost(expenses_list, specified_cost):
    """
    Filters the list, eliminating all the expenses with a cost smaller than
    a specified one, without modifying the actual list
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_cost: the specified cost
    :type specified_cost: int
    :return: the filtered list
    :rtype: list
    """

    return [element for element in expenses_list if get_cost(element) >= specified_cost]


def undo(expenses_manager_data):
    """
    Erases the most recent change made to the list
    The function gives the expenses list it's previous form
    :param expenses_manager_data: the necessary data for expenses management (expenses list, undo list)
    :return: -
    """
    undo_list =  get_undo_list(expenses_manager_data)

    if len(undo_list):
        list_previous_state = undo_list.pop()
        list_previous_state = copy_list_expenses(list_previous_state)
        set_current_list(expenses_manager_data,list_previous_state)

    else:
        raise ValueError("Nu se poate efectua undo.")


def create_tokens_and_parameters_list(operation_list):
    operation_list = operation_list.split(';')
    operation_token = []
    operation_param = []

    for operation in operation_list:
        if ':' in operation:
            operation = operation.split(':')
            operation_token.append(operation[0].strip())
            operation_param.append(operation[1].strip())
        else:
            operation_token.append(operation.strip())

    for index in range(len(operation_param)):
        if ',' in operation_param[index]:
            parameters = operation_param[index].split(',')
            for each in parameters:
                each = each.strip()
            operation_param[index] = parameters

    return operation_token, operation_param

def get_token(tokens: list):
    current_token = tokens[0]
    tokens.remove(tokens[0])

    return current_token

def get_param(params):
    current_param = params[0]
    params.remove(params[0])

    return current_param
