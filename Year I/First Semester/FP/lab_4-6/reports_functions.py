import math
from Domain.expense import get_day, get_cost, get_type, create_expense
from utils import copy_list_expenses, copy_expense


# ui<-t_manager<-domain
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
    Sum = 0
    for element in expenses_list:
        if get_type(element) == specified_type:
            Sum += get_cost(element)
    return Sum


def day_greatest_cost(expenses_list):
    """
    Determines the day of the expense with the greatest cost
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :return: the day of the expense with the greatest cost
    :rtype: int
    """
    the_day = -1  # this variable represents the day of the expense with the greatest cost
    greatest_cost = -math.inf

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



def test_sum_for_type():
    test_list = [create_expense(3, 129, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere'),
                 create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele'),
                 create_expense(30, 50, 'telefon')
                 ]
    assert sum_for_type(test_list, 'mancare') == 235
    assert sum_for_type(test_list, 'imbracaminte') == 430
    assert sum_for_type(test_list, 'altele') == 1000
    assert sum_for_type(test_list, 'telefon') == 179
    assert sum_for_type(test_list, 'intretinere') == 120


def test_day_greatest_cost():
    test_list = [create_expense(3, 129, 'telefon'), create_expense(5, 215, 'mancare')]
    assert day_greatest_cost(test_list) == 5
    test_list = [create_expense(9, 120, 'intretinere'), create_expense(13, 20, 'mancare')]
    assert day_greatest_cost(test_list) == 9
    test_list = [create_expense(23, 1000, 'altele'), create_expense(25, 253, 'altele')]
    assert day_greatest_cost(test_list) == 23
    test_list = [create_expense(30, 578, 'imbracaminte'), create_expense(30, 50, 'telefon')]
    assert day_greatest_cost(test_list) == 30


def test_expenses_by_cost():
    test_list = [create_expense(3, 120, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere'),
                 create_expense(13, 215, 'mancare'),
                 create_expense(15, 430, 'imbracaminte')
                 ]
    assert expenses_by_cost(test_list, 120) == [create_expense(3, 120, 'telefon'),
                                                create_expense(9, 120, 'intretinere')]
    assert expenses_by_cost(test_list, 215) == [create_expense(4, 215, 'mancare'),
                                                create_expense(13, 215, 'mancare')]
    assert expenses_by_cost(test_list, 430) == [create_expense(15, 430, 'imbracaminte')]
    assert expenses_by_cost(test_list, 1000) == []



def test_sorted_by_type():
    test_list = [create_expense(3, 129, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere'),
                 create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele'),
                 create_expense(30, 50, 'telefon'),
                 create_expense(12,13,'mancare')
                 ]
    sorted_list = [create_expense(23, 1000, 'altele'),
                   create_expense(15, 430, 'imbracaminte'),
                   create_expense(9, 120, 'intretinere'),
                   create_expense(4, 215, 'mancare'),
                   create_expense(13, 20, 'mancare'),
                   create_expense(12, 13, 'mancare'),
                   create_expense(30, 50, 'telefon'),
                   create_expense(3, 129, 'telefon'),
                   ] #incearca un bubble sort in care bagi conditie sa fie caelasi tip cand compari
    assert sorted_by_type(test_list) == sorted_list
    test_list = [create_expense(7,9,'telefon'),
                 create_expense(12,14,'altele'),
                 create_expense(22, 15,'intretinere')]
    sorted_list = [create_expense(12,14,'altele'),
                   create_expense(22, 15,'intretinere'),
                   create_expense(7,9,'telefon')]
    assert sorted_by_type(test_list) == sorted_list

