from domain.task import Task
from domain.validator import TaskValidator
from repository.memory_repository import TaskInMemoryRepository


class TaskController:
    def __init__(self, repository: TaskInMemoryRepository, task_validator: TaskValidator):
        self.__task_validator = task_validator
        self.__repo = repository

    def add_task(self, id, descriere: str, zi: int, luna: int, status: str) -> None:
        """
        Adauga un task in lista de task-uri
        :param task_list: lista de task-uri
        :type task_list: list
        :param task: task-ul de adaugat
        :type task: dict
        :return: -; modifica lista prin adaugarea la sfarsit a task-ului
        :rtype:
        :raises: ValueError daca task-ul de adaugat nu este valid, daca task-ul exista deja
        """

        task = Task(id, descriere, zi, luna, status)
        self.__task_validator.validate_task(task)
        self.__repo.store(task)

    def delete_task(self, id: int):
        """
        Sterge task dupa id
        :param id: id dupa care se sterge
        :type id: int
        :return: task-ul sters
        :rtype: Task
        :raises: ValueError daca nu exista task cu id dat
        """
        return self.__repo.delete(id)

    def filter_by_date(self, zi_start: int, luna_start: int, zi_end: int, luna_end: int) -> list:
        """
        Cauta un task cu data intre 2 date date
        :param task_list: lista de task-uri
        :param zi_start: ziua datei de inceput
        :param luna_start: luna datei de inceput
        :param zi_end: ziua datei de sfarsit
        :param luna_end: luna datei de sfarsit
        :return: o noua lista cu task-urile care sunt intre datele date
        """
        # TO-DO: refactor for cleaner version
        # See here some options: https://stackoverflow.com/questions/5464410/how-to-tell-if-a-date-is-between-two-other-dates)
        tasks_with_date_list = []
        date_start = (luna_start, zi_start)
        date_end = (luna_end, zi_end)
        for task in self.__repo.get_all():
            current_date = (task.get_luna_deadline(), task.get_zi_deadline())
            if date_start <= current_date <= date_end:
                tasks_with_date_list.append(task)

        return tasks_with_date_list

    def filter_by_description(self, description: str) -> list:
        """
        Returneaza lista cu task-urile care contin in descriere un string dat
        :param task_list: lista de task-uri
        :param description: substring-ul dupa care se cauta
        :return: o lista in care se regasesc doar task-urile care au in descriere string-ul dat
        """
        return [task for task in self.__repo.get_all() if description.lower() in task.get_descriere().lower()]

    def get_report_by_day(self) -> dict:
        """
        Face un raport de activitati pe data
        :param task_list: lista de task-uri
        :return: dictionar cu cheie data (str format din zi si luna) si valoare lista
                aferenta de task-uri care au deadline in ziua respectiva
        """
        day_dictionary = {}
        for task in self.__repo.get_all():
            if task.get_date() in day_dictionary:
                day_dictionary[task.get_date()].append(task)
            else:
                day_dictionary[task.get_date()] = [task]
        return day_dictionary

    def get_all_tasks(self) -> list:
        """
        Returneaza lista cu toate task-urile

        """
        return self.__repo.get_all()

    def add_default_tasks(self):
        self.add_task(1, 'Read book', 11, 10, 'pending')
        self.add_task(2, 'Host movie marathon', 5, 8, 'done')
        self.add_task(3, 'Travel to uncharted island', 10, 1, 'in-progress')
        self.add_task(4, 'Build treehouse', 12, 9, 'pending')
        self.add_task(5, 'Book Skydiving Adventure', 4, 4, 'done')
        self.add_task(6, 'Learn to ski', 21, 11, 'done')
        self.add_task(7, 'Master Art of Origami', 5, 8, 'in-progress')
        self.add_task(8, 'Dance to 80\'s music', 12, 9, 'pending')
        self.add_task(9, 'Learn to play guitar', 12, 9, 'done')
        self.add_task(10, 'Listen to Christmas music', 30, 12, 'done')

        # Extra-method

    def delete_by_status(self, status_to_delete: str) :
        """
        Sterge task-urile din list care au statusul dat
        :param status: statusul dupa care se sterge
        :return: numar de task-uri sterse
                lista se modifica prin eliminarea task-urilor cu statusul dat
        :rtype:int
        """

        # La seminar (217): implementare de mai jos
        # modificare doar la delete, pe baza de id - facem find task in Repo)
        # Cand apare problema in cadrul acestei implementari? Decomentati
        # codul si rulati test

        # lista_taskuri = self.__repo.get_all()
        # for task in lista_taskuri:
        #     if task.get_status() == status:
        #         print(len(lista_taskuri), len(self.__repo.get_all()))
        #         self.__repo.delete(task.get_id())

        # Modificat: stergere multipla din Repo cu argument functie
        return self.__repo.delete_multiple(lambda task: task.get_status() == status_to_delete)
