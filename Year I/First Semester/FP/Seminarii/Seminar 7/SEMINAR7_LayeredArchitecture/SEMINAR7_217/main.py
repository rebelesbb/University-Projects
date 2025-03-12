from domain.validator import TaskValidator
from repository.memory_repository import TaskInMemoryRepository
from service.service import TaskController
from ui.console import Console

repository = TaskInMemoryRepository()
validator = TaskValidator()
controller = TaskController(repository, validator)
console = Console(controller)
console.run()