from Domain.expense import get_type,get_cost,get_day,set_day,set_type,set_cost, create_expense

def copy_expense(expense):
    """
    Returns a copy of the expense
    :param expense: the expense
    :type expense: dict
    :return: the copy of the expense
    :rtype: dict
    """
    return create_expense(get_day(expense),get_cost(expense),get_type(expense))
def copy_list_expenses(expenses_list):
    """
    Creates a copy of an expenses list list
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :return: the copy of the list
    :rtype: list
    """
    copy_list = []
    for index in range(len(expenses_list)):
        expense_copy = copy_expense(expenses_list[index])
        copy_list.append(expense_copy)

    return copy_list

