from Utils.expense_utils import copy_expense

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