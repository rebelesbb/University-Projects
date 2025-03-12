from Domain.expense import get_type,get_cost,get_day, create_expense

def copy_expense(expense):
    """
    Returns a copy of the expense
    :param expense: the expense
    :type expense: dict
    :return: the copy of the expense
    :rtype: dict
    """
    return create_expense(get_day(expense),get_cost(expense),get_type(expense))