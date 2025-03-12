class TaskValidator:
    def __init__(self):
        pass

    def validate_task(self, task):
        """
        Valideaza un task dat
        :param task: task-ul care se valideaza
        :return: -
        :raises: ValueError daca task-ul nu e valid
        """
        errors = []
        if len(task.get_descriere()) < 2:
            errors.append("Descrierea nu este corecta. Trebuie sa fie mai lunga de 2 caractere.")

        if task.get_zi_deadline() > 31 or task.get_zi_deadline() < 1:
            errors.append("Ziua deadline nu poate fi decat intre 1-31.")

        if task.get_luna_deadline() > 12 or task.get_luna_deadline() < 1:
            errors.append("Luna deadline nu poate fi decat intre 1-12.")

        if task.get_status() not in ['pending', 'in-progress', 'done']:
            errors.append('Status incorect.')

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
