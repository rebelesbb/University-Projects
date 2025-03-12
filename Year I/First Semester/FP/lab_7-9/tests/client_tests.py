from domain.client import *


def test_client():
    last_generated_client_id = 200000
    client_nou = Client('Nume Prenume', 5000000000000)
    client_nou.generate_id(last_generated_client_id)
    validator = ClientValidator()

    try:
        validator.validate_client(client_nou)
        assert True
    except ValueError:
        assert False

    assert client_nou.get_name() == 'Nume Prenume'
    assert client_nou.get_cnp() == 5000000000000
    assert client_nou.get_id() == 200001

    client_nou = Client('Nume', 5000000000000)
    try:
        validator.validate_client(client_nou)
        assert False
    except ValueError:
        assert True

    client_nou = Client('Nume Prenume', 3000000000000)
    try:
        validator.validate_client(client_nou)
        assert False
    except ValueError:
        assert True

    client_nou = Client('Nume Prenume', 5000000)
    try:
        validator.validate_client(client_nou)
        assert False
    except ValueError:
        assert True
