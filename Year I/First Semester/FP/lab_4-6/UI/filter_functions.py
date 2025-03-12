from Domain.expense import get_type, get_cost, create_expense


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
    Filterst the list, eliminating all the expenses with a cost smaller than
    a sopecified one, without modifying the actual list
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_cost: the specified cost
    :type specified_cost: int
    :return: the filtered list
    :rtype: list
    """

    return [element for element in expenses_list if get_cost(element) >= specified_cost]


def test_filter_elements_by_specified_type():
    test_list = [create_expense(3, 129, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere')]
    assert filter_elements_by_specified_type(test_list, 'mancare') == [create_expense(3, 129, 'telefon'),
                                                                       create_expense(9, 120, 'intretinere')]

    test_list = [create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele')]
    assert filter_elements_by_specified_type(test_list, 'altele') == [create_expense(13, 20, 'mancare'),
                                                                      create_expense(15, 430, 'imbracaminte')]
    test_list = [create_expense(30, 578, 'imbracaminte'),
                 create_expense(30, 50, 'imbracaminte')]
    assert filter_elements_by_specified_type(test_list, 'imbracaminte') == []


def test_filter_elements_specified_cost():
    test_list = [create_expense(3, 129, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere')]
    copy_list = [create_expense(3, 129, 'telefon'),
                 create_expense(4, 215, 'mancare'),
                 create_expense(9, 120, 'intretinere')]
    assert filter_elements_specified_cost(test_list, 125) == [create_expense(3, 129, 'telefon'),
                                                              create_expense(4, 215, 'mancare')]
    assert copy_list == test_list  # to verify that the actual list was not modified
    test_list = [create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele')]
    assert filter_elements_specified_cost(test_list, 20) == test_list
    assert filter_elements_specified_cost(test_list, 1000) == [create_expense(23, 1000, 'altele')]
    assert filter_elements_specified_cost(test_list,2000) == []
