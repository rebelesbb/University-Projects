from domain.book import *


def test_book():
    last_generated_id = 100000
    test_book_ = Book('Carte', 'Carte foarte misto.', 'Autor')
    test_book_.generate_id(last_generated_id)
    validator = BookValidator()

    try:
        validator.validate_book(test_book_)
        assert True
    except ValueError:
        assert False

    assert test_book_.get_author() == 'Autor'
    assert test_book_.get_description() == 'Carte foarte misto.'
    assert test_book_.get_title() == 'Carte'
    assert test_book_.get_id() == 100001

    test_book_ = Book('Carte', 'Carte', 'Autor')
    try:
        validator.validate_book(test_book_)
        assert False
    except ValueError:
        assert True
