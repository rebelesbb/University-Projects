from tests.event_repo_tests import EventRepoTests
from tests.event_service_tests import EventServiceTest
from domain.validator import EventValidator
from repository.event_repo import EventRepository

def run_tests():
    event_repo_test = EventRepoTests()
    event_repo_test.run_tests()

    event_repo_test1 = EventRepository()
    event_validator = EventValidator()
    event_service_test = EventServiceTest(event_repo_test1, event_validator)
    event_service_test.run_tests()