from Domain.expense import get_day, get_type, create_expense
def delete_for_specified_day(expenses_list, specified_day):
    """
    Deletes all the expenses for a specified day
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_day: the specified day
    :type specified_day: int
    :return: -
    """
    for index in reversed(range(len(expenses_list))):
        if get_day(expenses_list[index]) == specified_day:
            del expenses_list[index]


def delete_for_specified_period(expenses_list, first_day, last_day):
    """
    Deletes all expenses for a specified period of the time
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param first_day: the first day of the time period
    :type first_day: int
    :param last_day: the last day of the time period
    :type last_day: int
    :return: -
    """
    for index in reversed(range(len(expenses_list))):
        if get_day(expenses_list[index]) >= first_day and get_day(expenses_list[index]) <= last_day:
            del expenses_list[index]


def delete_for_specified_type(expenses_list, specified_type):
    """
    Deletes all expenses for a specified type
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :param specified_type: the specified type
    :type specified_type: str
    :return: -
    """

    for index in reversed(range(len(expenses_list))):
        if get_type(expenses_list[index]) == specified_type:
            del expenses_list[index]


def test_delete_for_specified_day():
    test_list = [create_expense(3,129,'altele'),
                 create_expense(4,215,'altele')]
    delete_for_specified_day(test_list, 3)
    assert test_list == [create_expense(4,215,'altele')]

    test_list = [create_expense(9,215,'altele'),
                 create_expense(13,20,'mancare'),
                 create_expense(13,430,'imbracaminte')]
    delete_for_specified_day(test_list, 13)
    assert test_list == [create_expense(9,215,'altele')]

    test_list = [create_expense(30,253,'altele'),
                 create_expense(30,578,'imbracaminte'),
                 create_expense(30,50,'telefon')]
    delete_for_specified_day(test_list, 30)
    assert test_list == []

    test_list = [create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele')]
    delete_for_specified_day(test_list,13)
    assert test_list == [create_expense(15,430,'imbracaminte'),
                         create_expense(23,1000,'altele')]

def test_delete_for_specified_period():
    test_list = [create_expense(3,129,'altele'),
                 create_expense(4,215,'altele'),
                 create_expense(9,215,'altele'),
                 create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele'),
                 create_expense(30,578,'imbracaminte'),
                 create_expense(30,50,'telefon')]
    delete_for_specified_period(test_list, 9, 30)
    assert test_list == [create_expense(3,129,'altele'),
                         create_expense(4,215,'altele')]
    test_list = [create_expense(3,129,'altele'),
                 create_expense(4,215,'altele'),
                 create_expense(9,215,'altele')]
    delete_for_specified_period(test_list, 1, 3)
    assert test_list == [create_expense(4,215,'altele'),
                         create_expense(9,215,'altele')]
    test_list = [create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele')]
    delete_for_specified_period(test_list, 10, 20)
    assert test_list == [create_expense(23,1000,'altele'),
                         create_expense(25,253,'altele')]
    test_list = [create_expense(30,578,'imbracaminte'),
                 create_expense(30,50,'telefon')]
    delete_for_specified_period(test_list, 29, 32)
    assert test_list == []

def test_delete_for_specified_type():
    test_list = [create_expense(3,129,'altele'),
                 create_expense(4,215,'altele'),
                 create_expense(9,215,'altele'),
                 create_expense(13,20,'mancare'),
                 create_expense(15,430,'imbracaminte'),
                 create_expense(23,1000,'altele'),
                 create_expense(25,253,'altele'),
                 create_expense(30,578,'imbracaminte'),
                 create_expense(30,50,'telefon')]

    delete_for_specified_type(test_list, 'altele')
    assert test_list == [create_expense(13,20,'mancare'),
                         create_expense(15,430,'imbracaminte'),
                         create_expense(30,578,'imbracaminte'),
                         create_expense(30,50,'telefon')]

    delete_for_specified_type(test_list, 'imbracaminte')
    assert test_list == [create_expense(13,20,'mancare'),
                         create_expense(30,50,'telefon')]

    delete_for_specified_type(test_list, 'intretinere')
    assert test_list == [create_expense(13,20,'mancare'),
                         create_expense(30,50,'telefon')]

    delete_for_specified_type(test_list,'telefon')
    assert test_list == [create_expense(13,20,'mancare')]

    delete_for_specified_type(test_list,'mancare')
    assert test_list == []

