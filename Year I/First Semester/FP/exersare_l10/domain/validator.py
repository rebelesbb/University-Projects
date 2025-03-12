from domain.event import Event


class EventValidator:
    def __init__(self):
        pass

    def validate_event(self, event: Event):
        """
        Checks if the input date for an event is correct
        :param event: the event
        :return: -
        :raises ValueError if the description is shorter than 5 characters
                           if the month is not aa number between 1 and 12
                           if the day is not a number between 1 and 30
        """

        errors = []

        if len(event.get_description()) < 5:
            errors.append('Descrierea nu poate avea mai putin de 5 caractere.')

        date_info = [int(info.strip()) for info in event.get_date().split('-') if info != '']

        # checks the day
        if not 0 < date_info[0] <= 30:
            errors.append("Ziua intordusa nu este valida.")

        # checks the month
        if not 0 < date_info[1] <= 12:
            errors.append("Luna intordusa nu este valida.")

        time_info = [int(info.strip()) for info in event.get_time().split('-') if info != '']

        if not 0 <= time_info[0] <= 23 or not 0 <= time_info[1] <=59:
            errors.append("Timpul introdus in care evenimentul ar trebui sa se desfasoare nu este valid.")

        if len(errors):
            errors = '\n'.join(errors)
            raise ValueError(errors)
