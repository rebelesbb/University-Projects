from colorama import Fore, Style


def create_task(descriere: str, day: int, month: int, status: str) -> dict:
    """
    Creeaza un task
    :param descriere: descrierea task-ului
    :type descriere: str
    :param data: data task-ului (dd-mm)
    :type data: str
    :param status: status-ul task-ului
    :type status: str
    :return: task-ul creat
    :rtype: dict
    """

    return {'descriere': descriere, 'zi_deadline': day,
            'luna_deadline': month, 'status': status}


def get_description(task):
    return task['descriere']


def get_deadline_day(task):
    return task['zi_deadline']


def get_deadline_month(task):
    return task['luna_deadline']


def get_status(task):
    return task['status']


def get_date(task):
    return str(task['zi_deadline']) + '-' + str(task['luna_deadline'])


def set_description(task, new_description):
    task['descriere'] = new_description


def set_zi_deadline(task, new_day):
    task['zi_deadline'] = new_day


def set_luna_deadline(task, new_month):
    task['luna_deadline'] = new_month


def set_status(task, new_status):
    task['status'] = new_status


def to_str(task) -> str:
    return Fore.CYAN + get_description(task) + Fore.BLUE + ' | ' + str(get_deadline_day(task)) + '/' + str(
        get_deadline_month(task)) + Fore.MAGENTA + ' | ' + get_status(task) + Style.RESET_ALL


def validate_task(task):
    """
    Valideaza un task dat
    TASK VALID:
     --descriere cu lungime mai mare de 2
     --zi intre 1 si 31 si luna intre 1 si 12
     --status sa fie din multimea {pending, in-progress, done}

    :param task: task-ul care se valideaza
    :return: -
    :raises: ValueError daca task-ul nu e valid
    """
    errors = []
    if len(get_description(task)) < 2:
        errors.append("Descriere incorecta. Trebuie sa fie mai lunga de 2 caractere.")

    if get_deadline_day(task) < 1 or get_deadline_day(task) > 31:
        errors.append("Zi incorecta. Trebuie sa fie intre 1 si 31.")

    if get_deadline_month(task) < 1 or get_deadline_month(task) > 12:
        errors.append("Luna incorecta. Trebuie sa fie intre 1 si 12.")

    if get_status(task) not in ['pending', 'in-progress', 'done']:
        errors.append('Status incorect.')

    if len(errors) > 0:
        raise ValueError(errors)
