from tests.book_tests import test_book
from tests.book_repo_tests import TestBookRepo
from tests.book_service_tests import TestBookService
from repository.book_repo import BookInMemory
from service.book_service import BookService
from domain.book import BookValidator
from tests.client_tests import test_client
from tests.client_repo_tests import TestClientRepo
from tests.client_service_tests import TestClientService
from repository.client_repo import ClientInMemory
from service.client_service import ClientService
from domain.client import ClientValidator
from tests.rent_tests import test_rent
from tests.rent_repo_tests import TestRentRepo
from tests.rent_service_tests import TestRentService
from repository.rent_repo import RentInMemory
from service.rent_service import RentService
from domain.rent import RentValidator


def run_tests():
    # book tests
    test_book()

    book_repo_test = TestBookRepo()
    book_repo_test.run_tests()

    repo = BookInMemory()
    validator = BookValidator()
    book_service = BookService(validator, repo)
    book_service_test = TestBookService(book_service)
    book_service_test.run_tests()

    # client tests
    test_client()

    client_repo_test = TestClientRepo()
    client_repo_test.run_tests()

    repo = ClientInMemory()
    validator = ClientValidator()
    client_service = ClientService(validator, repo)
    client_service_test = TestClientService(client_service)
    client_service_test.run_tests()

    # rent tests
    test_rent()

    rent_repo_test = TestRentRepo()
    rent_repo_test.run_tests()

    repo = RentInMemory()
    validator = RentValidator()
    rent_service = RentService(validator, repo)
    rent_service_test = TestRentService(rent_service)
    rent_service_test.run_tests()
