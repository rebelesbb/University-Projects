def create_expenses_manager() -> dict:
    """

    :return:
    """
    undo_list = []
    expenses_list = []
    return {'undo_list':undo_list,
            'expenses_list': expenses_list}
def add_expense(expenses_list,expense):
    """
    Adds an expense to the list
    :param expenses_list: the list of expenses
    :type expenses_list: list
    :return: -
    """
    expenses_list.append(expense)

def get_undo_list(expenses_manager_data):
    return task_manager_data['undo_list']

def get_expenses_list(task_manager_data):
    return task_manager_data['expenses_list']

def set_current_list(task_manager_data, new_list):
    task_manager_data['expenses_list'] = new_list