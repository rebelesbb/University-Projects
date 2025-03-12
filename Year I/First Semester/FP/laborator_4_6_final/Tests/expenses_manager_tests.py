from List_manager.expenses_manager import *


def test_update_expense():
    test_manager_data = create_expenses_manager()
    test_list = [create_expense(12, 13, 'mancare'), create_expense(15, 1245, 'altele')]
    set_current_list(test_manager_data, test_list)
    new_expense = create_expense(1, 900, 'imbracaminte')
    update_expense(test_manager_data, 1, new_expense)
    assert test_list[0] == new_expense
    new_expense = create_expense(23, 10, 'telefon')
    update_expense(test_manager_data, 2, new_expense)
    assert test_list[1] == new_expense


def test_add_expense():
    test_manager_data = create_expenses_manager()
    test_list = []
    set_current_list(test_manager_data, test_list)
    assert len(get_expenses_list(test_manager_data)) == 0
    expense = create_expense(11, 13, 'mancare')
    add_expense(test_manager_data, expense)
    assert len(get_expenses_list(test_manager_data)) == 1
    assert get_day(get_expenses_list(test_manager_data)[0]) == 11


def test_delete_for_specified_day():
    test_manager_data = create_expenses_manager()

    test_list = [create_expense(3, 129, 'altele'),
                 create_expense(4, 215, 'altele')]
    set_current_list(test_manager_data, test_list)
    delete_for_specified_day(test_manager_data, 3)
    assert get_expenses_list(test_manager_data) == [create_expense(4, 215, 'altele')]

    test_list = [create_expense(9, 215, 'altele'),
                 create_expense(13, 20, 'mancare'),
                 create_expense(13, 430, 'imbracaminte')]
    set_current_list(test_manager_data, test_list)
    delete_for_specified_day(test_manager_data, 13)
    assert get_expenses_list(test_manager_data) == [create_expense(9, 215, 'altele')]

    test_list = [create_expense(30, 253, 'altele'),
                 create_expense(30, 578, 'imbracaminte'),
                 create_expense(30, 50, 'telefon')]

    set_current_list(test_manager_data, test_list)
    delete_for_specified_day(test_manager_data, 30)
    assert get_expenses_list(test_manager_data) == []

    test_list = [create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele')]
    set_current_list(test_manager_data, test_list)
    delete_for_specified_day(test_manager_data, 13)
    assert get_expenses_list(test_manager_data) == [create_expense(15, 430, 'imbracaminte'),
                                                    create_expense(23, 1000, 'altele')]


def test_delete_for_specified_period():
    test_manager_data = create_expenses_manager()
    test_list = [create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(23, 1000, 'altele'),
                 create_expense(25, 253, 'altele')]
    set_current_list(test_manager_data, test_list)
    delete_for_specified_period(test_manager_data, 10, 20)
    assert get_expenses_list(test_manager_data) == [create_expense(23, 1000, 'altele'),
                                                    create_expense(25, 253, 'altele')]

    test_list = [create_expense(30, 578, 'imbracaminte'),
                 create_expense(30, 50, 'telefon')]
    set_current_list(test_manager_data, test_list)
    try:
        delete_for_specified_period(test_manager_data, 0, 19)
        assert False
    except:
        assert True
    delete_for_specified_period(test_manager_data, 29, 31)
    assert get_expenses_list(test_manager_data) == []


def test_delete_for_specified_type():
    test_list_manager = create_expenses_manager()

    test_list = [create_expense(13, 20, 'mancare'),
                 create_expense(15, 430, 'imbracaminte'),
                 create_expense(30, 578, 'imbracaminte'),
                 create_expense(30, 50, 'mancare')]

    set_current_list(test_list_manager, test_list)
    delete_for_specified_type(test_list_manager,'imbracaminte')
    assert get_expenses_list(test_list_manager) == [create_expense(13, 20, 'mancare'),
                                                    create_expense(30, 50, 'mancare')]

    delete_for_specified_type(test_list_manager, 'mancare')
    assert get_expenses_list(test_list_manager) == []

    try:
        delete_for_specified_type(test_list_manager,'bautura')
        assert False
    except:
        assert True


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

def test_undo():
    test_manager_data = create_expenses_manager()

    add_expense(test_manager_data, create_expense(12,13,'mancare'))
    assert len(get_expenses_list(test_manager_data)) == 1
    undo(test_manager_data)
    assert len(get_expenses_list(test_manager_data)) == 0
    try:
        undo(test_manager_data)
        assert False
    except ValueError:
        assert True

    add_expense(test_manager_data, create_expense(12,13,'mancare'))
    update_expense(test_manager_data,1,create_expense(10,20,'intretinere'))
    undo(test_manager_data)
    assert get_expenses_list(test_manager_data) == [create_expense(12,13,'mancare')]

    delete_for_specified_day(test_manager_data, 12)
    assert get_expenses_list(test_manager_data) == []
    undo(test_manager_data)
    assert get_expenses_list(test_manager_data) == [create_expense(12,13,'mancare')]

    test_list = [create_expense(1,1,'mancare'),
                 create_expense(2,2,'intretinere'),
                 create_expense(3,3,'mancare')]

    set_current_list(test_manager_data,copy_list_expenses(test_list))

    delete_for_specified_period(test_manager_data,1,2)
    assert get_expenses_list(test_manager_data) == [create_expense(3,3,'mancare')]
    undo(test_manager_data)
    assert get_expenses_list(test_manager_data) == test_list

    delete_for_specified_type(test_manager_data,'mancare')
    delete_for_specified_type(test_manager_data,'intretinere')
    assert get_expenses_list(test_manager_data) == []
    undo(test_manager_data)
    assert get_expenses_list(test_manager_data) == [create_expense(2,2,'intretinere')]
    undo(test_manager_data)
    assert get_expenses_list(test_manager_data) == test_list

def test_expenses_management_functions():
    test_add_expense()
    test_update_expense()
    test_delete_for_specified_day()
    test_delete_for_specified_day()
    test_delete_for_specified_period()
    test_delete_for_specified_type()
    test_search_greater_than_cost()
    test_search_before_day_smaller_than_cost()
    test_search_by_type()
    test_sum_for_type()
    test_day_greatest_cost()
    test_expenses_by_cost()
    test_sorted_by_type()
    test_filter_elements_specified_cost()
    test_filter_elements_by_specified_type()
    test_undo()
