from repository.event_repo import EventRepository
from service.event_service import EventService
from domain.validator import EventValidator
from ui.console import Console
from tests.all_tests_run import run_tests

run_tests()

event_repo = EventRepository()
event_validator = EventValidator()
event_service = EventService(event_repo, event_validator)

console = Console(event_service)
console.start_console()

