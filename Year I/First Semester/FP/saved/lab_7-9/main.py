from ui.console import Console
from domain.book import BookValidator
from repository.book_repo import BookInMemory
from service.book_service import BookController
from domain.client import ClientValidator
from repository.client_repo import ClientInMemory
from service.client_service import ClientController
from domain.rent import RentValidator
from repository.rent_repo import RentInMemory
from service.rent_service import RentController

book_repository = BookInMemory()
book_validator = BookValidator()
book_controller = BookController(book_validator, book_repository)

client_repository = ClientInMemory()
client_validator = ClientValidator()
client_controller = ClientController(client_validator, client_repository)

rent_repository = RentInMemory()
rent_validator = RentValidator()
rent_controller = RentController(rent_validator, rent_repository)

console = Console(book_controller, client_controller, rent_controller)
console.start_menu()