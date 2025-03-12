from repository.event_repo import EventRepository
from domain.event import Event

class EventRepoTests:
    def __init__(self):
        self.test_repo = EventRepository()

    def test_store(self):
        assert self.test_repo.size() == 0
        event = Event('12-12-2023','12-45','football game')
        self.test_repo.store(event)
        assert self.test_repo.size() == 1

        assert event == self.test_repo.get_event(0)
        assert event.get_id() == self.test_repo.get_event(0).get_id()

        event = Event('11-11-2009','12-50','festival')
        self.test_repo.store(event)
        assert self.test_repo.size() == 2

    def test_find(self):
        event = Event('12-12-2023', '12-45', 'football game')
        assert self.test_repo.find(200001) == event

        event = Event('11-11-2009','12-50','festival')
        assert self.test_repo.find(200002) == event

        assert self.test_repo.find(200003) is None

    def test_delete(self):
        assert self.test_repo.size() == 2
        event = Event('12-12-2023','12-45','football game')
        self.test_repo.delete(event)

        assert self.test_repo.size() == 1

        event = Event('11-11-2009','12-50','festival')
        assert self.test_repo.get_event(0) == event
        self.test_repo.delete(event)

        assert self.test_repo.size() == 0

    def test_modify(self):
        event = Event('12-12-2023', '12-45', 'football game')
        self.test_repo.store(event)
        new_event = Event('11-11-2009','12-50','festival')
        self.test_repo.modify(event, new_event)

        assert new_event == self.test_repo.get_event(0)

        self.test_repo.modify(new_event, event)
        assert event == self.test_repo.get_event(0)


    def run_tests(self):
        self.test_store()
        self.test_find()
        self.test_delete()
        self.test_modify()
