from ui.console import Console
from domain.book import BookValidator
from repository.book_repo import BookInMemory, BookInFile
from service.book_service import BookService
from domain.client import ClientValidator
from repository.client_repo import ClientInMemory, ClientInFile
from service.client_service import ClientService
from domain.rent import RentValidator
from repository.rent_repo import RentInMemory, RentInFile
from service.rent_service import RentService
from tests.all_tests import run_tests

#run_tests()

book_repository = BookInFile('data/books.txt')
book_validator = BookValidator()
book_controller = BookService(book_validator, book_repository)

client_repository = ClientInFile('data/clients.txt')
client_validator = ClientValidator()
client_controller = ClientService(client_validator, client_repository)

rent_repository = RentInFile('data/rent.txt', book_repository, client_repository)
rent_validator = RentValidator()
rent_controller = RentService(rent_validator, rent_repository)

console = Console(book_controller, client_controller, rent_controller)
console.start_menu()
