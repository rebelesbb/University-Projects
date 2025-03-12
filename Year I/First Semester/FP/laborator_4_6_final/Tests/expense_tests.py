from Domain.expense import create_expense, get_cost, get_day, get_type, validate_expense

def test_create_expense():
    expense = create_expense(12,234,'mancare')
    assert get_day(expense) == 12
    assert get_cost(expense) == 234
    assert get_type(expense) == 'mancare'

def test_validate_expense():
    expense = create_expense(11, 12, 'mancare')
    try:
        validate_expense(expense)
        assert True
    except ValueError:
        assert False

    expense = create_expense(0,123,'mancare')
    try:
        validate_expense(expense)
        assert False
    except ValueError:
        assert True

    expense = create_expense(11,12,'bautura')
    try:
        validate_expense(expense)
        assert False
    except ValueError:
        assert True

def test_expense_functions():
    test_create_expense()
    test_validate_expense()
