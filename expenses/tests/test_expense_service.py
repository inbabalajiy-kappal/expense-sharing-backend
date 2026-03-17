from expenses.services.expense_service import ExpenseService


def test_service_exists():

    service = ExpenseService()

    assert service is not None