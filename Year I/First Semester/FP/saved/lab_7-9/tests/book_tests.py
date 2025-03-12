from domain.book import *

def test_book():
    last_generated_id = 100000
    test_book = Book('Carte', 'Carte foarte misto.', 'Autor')
    test_book.generate_id(last_generated_id)
    validator = BookValidator()

    try:
        validator.validate_book(test_book)
        assert True
    except ValueError:
        assert False

    assert test_book.get_author() == 'Autor'
    assert test_book.get_description() == 'Carte foarte misto.'
    assert test_book.get_title() == 'Carte'
    assert test_book.get_id() == 100001

    test_book = Book('Carte', 'Carte', 100)
    try:
        validator.validate_book(test_book)
        assert False
    except ValueError:
        assert True


test_book()