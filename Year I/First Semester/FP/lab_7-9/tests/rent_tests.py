from domain.rent import Rent, RentValidator
from domain.book import Book
from domain.client import Client
from datetime import date

def test_rent():
    previous_id = 400000
    book = Book('Carte 1','Descrierea primei carti','Autor 1')
    book.generate_id(100000)
    client = Client('Nume Prenume',5000000467382)
    client.generate_id(200000)
    rent = Rent(book, client)
    rent.generate_id(previous_id)

    assert rent.get_book() == book
    assert rent.get_client() == client
    assert rent.get_id() == 400001
    assert rent.get_rent_date() == date.today()
    assert rent.get_return_date() is None



