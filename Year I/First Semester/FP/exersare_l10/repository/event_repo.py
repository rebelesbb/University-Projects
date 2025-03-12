from domain.event import Event


class EventRepository:
    def __init__(self):
        self.__event_list = []
        self.__current_id = 200001

    def store(self, event: Event):
        """
        Stores an event into the event list
        :param event: the event to be stored
        :return: -
        """
        event.set_id(self.__current_id)
        self.__current_id += 1
        self.__event_list.append(event)

    def delete(self, event: Event):
        """
        Deletes an event from the list of events
        :param event: the eb=vent to be deleted
        :return: -
        """
        self.__event_list.remove(event)

    def modify(self, event: Event, updated_event: Event):
        """
        Modifies an event from the list of events
        :param event: the event to be modified
        :param updated_event: the updated information of the event
        :return: -
        """
        self.__event_list[self.__event_list.index(event)] = updated_event

    def find(self, event_id: int):
        """
        Finds an event in the list of events by its id
        :param event_id: the id of the event to be found
        :return: the event if found else None
        """
        for event in self.__event_list:
            if event.get_id() == event_id:
                return event
        return None

    def get_all(self):
        return self.__event_list

    def get_event(self, index):
        return self.__event_list[index]

    def size(self):
        return len(self.__event_list)
