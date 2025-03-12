from service.event_service import EventService
from domain.validator import EventValidator
from domain.event import Event
from repository.event_repo import EventRepository
class EventServiceTest:
    def __init__(self, repo: EventRepository, valid: EventValidator):
        self.__test_service = EventService(repo, valid)

    def test_add_event(self):

        assert self.__test_service.get_size() == 0

        event_date = '12-12-2023'
        event_time = '12-45'
        event_description = 'football game'
        event = Event(event_date, event_time, event_description)
        self.__test_service.add_event(event_date, event_time, event_description)

        assert self.__test_service.get_size() == 1

        assert self.__test_service.get_event(0) == event
        assert self.__test_service.get_event(0).get_id() == 200001

        event_date = '14-07-2000'
        event_time = '12-34'
        event_description = 'festival'
        self.__test_service.add_event(event_date, event_time, event_description)

        assert self.__test_service.get_size() == 2
        assert self.__test_service.get_event(1).get_id() == 200002

        try:
            event_date = '14-25-2000'
            event_time = '12-34'
            event_description = 'festival'
            self.__test_service.add_event(event_date, event_time, event_description)
            assert False
        except:
            assert True

    def test_search_event(self):
        event_to_find = self.__test_service.get_event(0)
        assert self.__test_service.search_event(200001) == event_to_find

        event_to_find = self.__test_service.get_event(1)
        assert self.__test_service.search_event(200002) == event_to_find

        assert self.__test_service.search_event(200003) is None

        try:
            self.__test_service.search_event(1)
            assert False
        except:
            assert True

    def test_delete_event(self):
        assert self.__test_service.get_size() == 2

        self.__test_service.delete_event(200001)
        assert self.__test_service.get_size() == 1

        event_date = '14-07-2000'
        event_time = '12-34'
        event_description = 'festival'
        event = Event(event_date, event_time, event_description)
        assert self.__test_service.get_event(0) == event

        self.__test_service.delete_event(200002)
        assert self.__test_service.get_size() == 0

    def test_update_event(self):
        event_date = '12-12-2023'
        event_time = '12-45'
        event_description = 'football game'
        event = Event(event_date, event_time, event_description)
        self.__test_service.add_event(event_date, event_time, event_description)

        event_date = '14-07-2000'
        event_time = '12-34'
        event_description = 'festival'
        new_event = Event(event_date, event_time, event_description)

        self.__test_service.update_event(200003, event_date, event_time, event_description)
        assert new_event == self.__test_service.get_event(0)
        assert self.__test_service.get_event(0).get_id() == 200003




    def run_tests(self):
        self.test_add_event()
        self.test_search_event()
        self.test_delete_event()
        self.test_update_event()
