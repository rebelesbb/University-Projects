from Domain.expense import get_day, get_cost, get_type, create_expense
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

    new_list = []

    for element in expenses_list:
        if get_day(element) < specified_day and get_cost(element) < specified_cost:
            new_list.append(element)

    return new_list

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
    new_list = []

    for element in expenses_list:
        if get_type(element) == specified_type:
            new_list.append(element)

    return new_list

def test_search_greater_than_cost():
    test_list = [create_expense(3,129,'telefon'),
                 create_expense(4,215,'mancare'),
                 create_expense(9,120,'intretinere')]

    assert search_greater_than_cost(test_list, 200) == [create_expense(4,215,'mancare')]
    test_list = [create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele')]
    assert search_greater_than_cost(test_list, 150) == [create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele')]
    test_list = [ create_expense(28,578,'imbracaminte'),
                  create_expense(30,50,'telefon'),
                  create_expense(30,217,'altele')]
    assert search_greater_than_cost(test_list, 1000) == []

def test_search_before_day_smaller_than_cost():
    test_list = [create_expense(3,129,'telefon'),
                 create_expense(4,215,'mancare'),
                 create_expense(9,120,'intretinere')]
    assert search_before_day_smaller_than_cost(test_list, 9, 200) == [create_expense(3,129,'telefon')]

    test_list = [create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele')]
    assert search_before_day_smaller_than_cost(test_list,25,1000) == [create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte')]

    test_list = [ create_expense(28,578,'imbracaminte'),
                  create_expense(30,50,'telefon'),
                  create_expense(30,217,'altele')]
    assert search_before_day_smaller_than_cost(test_list,30,123) == []

def test_search_by_type():
    test_list = [create_expense(3,129,'telefon'),
                 create_expense(4,215,'mancare'),
                 create_expense(9,120,'intretinere')]
    assert search_by_type(test_list, 'telefon') == [create_expense(3,129,'telefon')]
    test_list = [create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele')]
    assert search_by_type(test_list, 'altele') == [create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele')]
    assert search_by_type(test_list, 'imbracaminte') == [create_expense(15,430,'imbracaminte')]
    assert search_by_type(test_list, 'telefon') == []