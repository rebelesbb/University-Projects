class Event:
    def __init__(self, event_date: str, event_time: str, event_description: str):
        self.__id = None
        self.__date = event_date
        self.__time = event_time
        self.__description = event_description

    def __str__(self):
        return str(self.__id) + ' | ' + self.__date + ' | ' + self.__time + ' | ' + self.__description

    def __eq__(self, other):
        if self.__date == other.get_date() and self.__time == other.get_time() \
                and self.__description == other.get_description():
            return True
        return False

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def set_date(self, other):
        self.__date = other

    def set_time(self, other):
        self.__time = other

    def set_description(self, other):
        self.__description = other

    def set_id(self, other):
        self.__id = other
