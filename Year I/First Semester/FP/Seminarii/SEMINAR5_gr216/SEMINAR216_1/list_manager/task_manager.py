from domain.task import create_task, get_description, get_deadline_day, get_deadline_month, get_status, validate_task, \
    get_date
from utils.list_utils import make_list_copy


# Functii care ne ajuta sa ascundem reprezentarea acestui "manager"
# de restul aplicatiei
# Ca si get_... de la task, nu fac altceva decat sa imi returneze informatia
# aferenta entitatii pe care o trimit ca parametru
# dar avantajul accesarii informatiei astfel si nu direct,
# utilizand sintaxa specifica de dictionar sau lista peste tot
# unde trebuie sa accesez aceasta informatie
# este cand apare o schimbare: daca folosesc get, set
# nu depind de reprezentare - poate sa fie orice structura pe care o consider potrivita
# in "spate", in care imi tin informatia, si pot sa schimb rapid daca ma razgandesc
# ex. daca peste tot in aplicatie folosesc get_descriere, depind doar
# de specificatia lui get_descriere(task) (returneaza descrierea task-ului dat),
# pentru restul aplicatiei nu conteaza daca informatia a fost luata din dictionar, lista
# sau orice alta structura

# Analog - Daca ulterior imi tin astfel datele de task manager in : [current_task_list, undo_list]
# sa nu fie nevoie sa schimb in aplicatie decat aici

def create_task_manager() -> dict:
    """
        Creeaza o structura prin care gestionam datele din aplicatie
        :return: dictionar cu 2 chei:
                current_task_list: lista curenta de task-uri (lista de lucru)
                undo_list: lista de undo
        """
    undo_list = []
    task_list = []
    return {'undo_list': undo_list,
            'current_task_list': task_list}


def get_undo_list(task_manager_data):
    return task_manager_data['undo_list']


def get_current_list(task_manager_data):
    return task_manager_data['current_task_list']


def set_current_list(task_manager_data, new_list):
    task_manager_data['current_task_list'] = new_list


def add_state_to_undo(task_manager_data):
    """
    Adds the current state of the list to the undo list (stack)
    :param task_manager_data: dictionar care contine lista de undo si lista curenta
    :return: -; lista de undo se modifica prin adaugarea starii curente a listei la sfarsit
    """
    task_list = get_current_list(task_manager_data)
    undo_list = get_undo_list(task_manager_data)
    undo_list.append(make_list_copy(task_list))


def add_task(task_manager_data, descriere: str, day: int, month: int, status: str):
    """
    Adauga un task in lista de task-uri
    :param task_manager_data: datele necesare pentru gestiune (undo list, lista curenta)
    :param descriere: descrierea task-ului de adaugat
    :param day: ziua task-ului de adaugat
    :param month: luna task-ului de adaugat
    :param status: statusul task-ului de adaugat
    :return: -; lista curenta se modifica prin adaugarea task-ului creat
    :raises: ValueError daca task-ul nu este valid
    """
    task = create_task(descriere, day, month, status)
    validate_task(task)

    add_state_to_undo(task_manager_data)

    task_list = get_current_list(task_manager_data)
    task_list.append(task)


def undo(task_manager_data) -> None:
    """
    Anuleaza ultima operatie
    :return: -
    :raises ValueError daca nu se mai poate face undo
    """

    undo_list = get_undo_list(task_manager_data)
    if len(undo_list) > 0:
        previous_list = undo_list.pop()
        set_current_list(task_manager_data, previous_list)
    else:
        raise ValueError("Nu se mai poate face undo.")


def add_default_tasks(task_list):
    task1 = create_task('Read book', 11, 10, 'pending')
    task2 = create_task('Host movie marathon', 5, 8, 'done')
    task3 = create_task('Travel to uncharted island', 10, 1, 'in-progress')
    task4 = create_task('Build treehouse', 12, 9, 'pending')
    task5 = create_task('Book Skydiving Adventure', 4, 4, 'done')
    task6 = create_task('Learn to ski', 21, 11, 'done')
    task7 = create_task('Master Art of Origami', 5, 8, 'in-progress')
    task8 = create_task('Dance to 80\'s music', 12, 9, 'pending')
    task9 = create_task('Learn to play guitar', 12, 9, 'done')

    task_list.extend([task1, task2, task3, task4, task5, task6, task7, task8, task9])


def search_task_by_date(lista: list, ziua_start: int, luna_start: int, ziua_finish: int, luna_finish: int) -> bool:
    """
    Cauta un task care are data deadline intre datele date
    :param lista lista de task-uri in care se cauta
    :param ziua_start ziua datei de inceput
    :param luna_start luna datei de inceput
    :param ziua_finish ziua datei de final
    :param luna_finish luna datei de final
    :return: True cand exista un task intre acele date si False contrar
    """

    # TO-DO: refactor for cleaner version
    # See here some options: https://stackoverflow.com/questions/5464410/how-to-tell-if-a-date-is-between-two-other-dates)

    for task in lista:
        if luna_finish > get_deadline_month(task) > luna_start:
            return True
        elif luna_start == luna_finish == get_deadline_month(task):
            if ziua_start <= get_deadline_day(task) <= ziua_finish:
                return True
        elif get_deadline_month(task) == luna_start:
            if luna_finish > get_deadline_month(task) and get_deadline_day(task) >= ziua_start:
                return True
        elif get_deadline_month(task) == luna_finish:
            if luna_start < get_deadline_month(task) and get_deadline_day(task) <= ziua_finish:
                return True
    return False


def delete_task_by_description(task_manager_data, descriere):
    """
    Sterge task-ul cu descrierea data din lista
    :param task_manager_data: datele necesare pentru gestiunea task-urilor
    :param descriere: descrierea data
    :return: -; lista se modifica prin eliminarea task-ului cu descriere data
                daca aceasta exista
    """

    # Ce se intampla daca nu sterg nimic? Se va actualiza/adauga ceva in
    # lista de undo?
    add_state_to_undo(task_manager_data)
    task_list = get_current_list(task_manager_data)

    deleted = False
    for i in reversed(range(len(task_list))):
        if get_description(task_list[i]) == descriere:
            deleted = True
            task_list.remove(task_list[i])
    if not deleted:
        raise IndexError("Nu exista task cu descrierea data.")


def delete_by_status(task_manager_data: dict, status: str) -> None:
    """
    Sterge task-urile din list care au statusul dat
    :param task_list: lista de task-uri
    :param status: statusul dupa care se sterge
    :return: -; lista se modifica prin eliminarea task-urilor cu statusul dat
    """

    # Ar trebui sa fac add_state_to_undo in while, de fiecare data cand sterg ceva?
    # I.e. undo pentru aceasta operatie sa insemne undo pentru fiecare eventuala stergere?

    # Sau undo pentru aceasta operatie sa insemne revenirea la lista de dinaintea stergerilor
    # multiple?

    # Ce se intampla daca nu sterg nimic?

    add_state_to_undo(task_manager_data)

    task_list = get_current_list(task_manager_data)
    current_list_length = len(task_list)
    i = 0
    while i < current_list_length:
        task = task_list[i]
        if get_status(task) == status:
            task_list.pop(i)
            current_list_length -= 1
        else:
            i += 1


def filter_by_description(task_list: list, description: str) -> list:
    """
    Returneaza lista cu task-urile care contin in descriere un string dat
    :param task_list: lista de task-uri
    :param description: substring-ul dupa care se cauta
    :return: o lista in care se regasesc doar task-urile care au in descriere string-ul dat
    """
    return [task for task in task_list if description.lower() in get_description(task).lower()]


def get_report_by_day(task_list: list) -> dict:
    """
    Face un raport de activitati pe data
    :param task_list: lista de task-uri
    :return: dictionar cu cheie data (str format din zi si luna) si valoare lista
            aferenta de task-uri care au deadline in ziua respectiva
    """
    day_dictionary = {}
    for task in task_list:
        if get_date(task) in day_dictionary:
            day_dictionary[get_date(task)].append(task)
        else:
            day_dictionary[get_date(task)] = [task]
    return day_dictionary
