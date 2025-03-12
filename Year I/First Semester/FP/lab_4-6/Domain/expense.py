
def get_day(expense):
    return expense['day']
def get_cost(expense):
    return expense['cost']
def get_type(expense):
    return expense['type']

def set_day(expense, day):
    expense[0] = day

def set_cost(expense, cost):
    expense['cost'] = cost

def set_type(expense, type):
    expense['type'] = type


"""
def get_day(expense):
    return expense[0]
def get_cost(expense):
    return expense[1]
def get_type(expense):
    return expense[2]

def set_day(expense, day):
    expense[0] = day

def set_cost(expense, cost):
    expense[1] = cost

def set_type(expense, type):
    expense[2] = type
"""
def create_expense(day, cost, type):
    """
    Creates a new expense
    :return: the expense
    :rtype: dict
    """
    expense = {'day': day, 'cost': cost, 'type': type}
    #expense = [day, cost, type]
    return expense
