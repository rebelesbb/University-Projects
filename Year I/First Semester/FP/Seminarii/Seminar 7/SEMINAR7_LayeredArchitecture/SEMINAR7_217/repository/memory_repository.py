from domain.task import Task


class TaskInMemoryRepository:
    def __init__(self):
        self.__task_list = []

    def store(self, task: Task):
        """
        Adauga un task in lista de task-uri
        :param task: task-ul de adaugat
        :type task: Task
        :return: -; lista de task-uri se modifica prin adaugarea la sfarsit a task-ului dat
        :rtype: -;
        :raises: ValueError daca exista deja task cu id-ul dat
        """

        # verificam daca task-ul exista deja -
        # dar definim ce inseamna ca exista deja: are acelasi id, are aceeasi descriere si date, etc...
        # In aceasta varianta: egalitate inseamna ca 2 task-uri au acelasi id
        if self.find(task.get_id()):
            raise ValueError("Exista deja task cu acest id.")
        self.__task_list.append(task)

    # Functie ok - dar in anumite circumstante, m-ar ajuta mai mult sa imi returneze
    # direct task-ul cu id-ul dat
    # si de acolo pot verifica daca am task cu id dat sau nu (returned_task is (not) None)
    # vezi implementare mai jos
    # def find(self, id):
    #     """
    #     Cauta task cu id-ul dat
    #     :param id: id-ul pe care il cautam
    #     :type id: int
    #     :return: True daca exista deja task cu id dat, fals altfel
    #     :rtype: bool
    #     """
    #     for task in self.__task_list:
    #         if task.get_id() == id:
    #             return True
    #     return False

    def find(self, id):
        """
        Gaseste task-ul cu id dat
        :param id: id-ul cautat
        :type id: int
        :return: task-ul cu id dat
        :rtype: Task
        """
        for task in self.__task_list:
            if task.get_id() == id:
                return task
        return None

    def update(self, id, modified_task):
        """
        Modifica un task dat
        :param id: id-ul task-ului care se modifica
        :type id: int
        :param modified_task: task-ul care contine datele modificate
        :type modified_task: Task
        :return: task-ul modificat
        :rtype: Task
        """
        # TO-DO: How to implement update?
        pass

    def delete(self, id):
        """
        Sterge task cu id dat
        :param id: id-ul dupa care se sterge
        :type id: int
        :return: task-ul sters
        :rtype:Task
        """

        task_to_delete = self.find(id)
        if task_to_delete is None:
            raise ValueError("Nu exista task cu id dat.")

        self.__task_list.remove(task_to_delete)
        return task_to_delete

    def get_all(self) -> list:
        """
        Returneaza intreaga lista de task-uri
        """
        return self.__task_list

    def size(self):
        return len(self.__task_list)

    # Extra-function
    def delete_multiple(self, filter_function):
        """
        Elimina task-uri pe baza unui anumit criteriu
        :param filter_function: functia dupa care se filtreaza
        :type filter_function: function
        :return: numarul de task-uri sterse
        :rtype: int
        """
        initial_no_tasks = self.size()
        self.__task_list = [task for task in self.__task_list if not filter_function(task)]
        return initial_no_tasks - self.size()
