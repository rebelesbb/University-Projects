from repository.event_repo import EventRepository
from domain.event import Event
from domain.validator import EventValidator

class EventService:
    def __init__(self, repository: EventRepository, validator: EventValidator):
        self.__repo = repository
        self.__validator = validator

    def add_event(self, event_date: str, event_time: str, event_description: str):
        """
        Adds an event to the list of events
        :param event_date: the date of the event
        :param event_time: the time when the event takes place
        :param event_description: the description of the event
        :return: -
        """
        new_event = Event(event_date, event_time, event_description)
        self.__validator.validate_event(new_event)
        self.__repo.store(new_event)

    def delete_event(self, event_id):
        """
        Deletes an event from the list
        :param event_id: the id of the event
        :return: -
        """
        if 200000 < event_id:
            event = self.__repo.find(event_id)
            self.__repo.delete(event)
        else:
            raise ValueError("ID-ul introdus nu este valid.")

    def update_event(self, event_id: int, new_date: str, new_time: str, new_description: str):
        """
        Updates an event from the list
        :param event_id: the id of the event to be updated
        :param new_date: the new date
        :param new_time: the new time
        :param new_description: the new description
        :return: -
        """
        if 200000 < event_id and self.__repo.find(event_id) is not None:
            new_event = Event(new_date, new_time, new_description)
            self.__validator.validate_event(new_event)

            event_to_update = self.__repo.find(event_id)
            new_event.set_id(event_to_update.get_id())

            self.__repo.modify(event_to_update, new_event)

        else:
            raise ValueError("ID-ul introdus nu este valid.")

    def search_event(self, event_id):
        """
        Searches for an event
        :param event_id: the id of the event to be found
        :return: the event if found, else None
        """
        if 200000 < event_id:
            return self.__repo.find(event_id)
        else:
            raise ValueError("ID-ul introdus nu este valid.")


    def get_all_events(self):
        return self.__repo.get_all()

    def get_size(self):
        return self.__repo.size()

    def get_event(self, index):
        return self.__repo.get_event(index)

