from expenses.services.expense_service import ExpenseService


# ---------------------------------------------------------------------------
# Fakes
# ---------------------------------------------------------------------------

class FakeUser:

    def __init__(self, user_id):
        self.id = user_id


class FakeParticipant:

    def __init__(self, user):
        self.user = user


class FakeParticipantSet:

    def __init__(self, participants):
        self._participants = participants

    def all(self):
        return self._participants


class FakeExpense:

    def __init__(self, expense_id, payer_id=1, amount=100, split_type="EQUAL"):
        self.id = expense_id
        self.amount = amount
        self.split_type = split_type
        self.created_at = "2026-01-01"
        self.payer = FakeUser(payer_id)
        self.participants = FakeParticipantSet(
            [FakeParticipant(FakeUser(payer_id))]
        )


class FakeExpenseManager:

    def __init__(self, expenses):
        self._expenses = expenses

    def all(self):
        return self._expenses


class FakeExpenseModel:

    def __init__(self, expenses):
        self.objects = FakeExpenseManager(expenses)


class FakeBalance:

    def __init__(self, debtor_id, creditor_id, amount):
        self.debtor = FakeUser(debtor_id)
        self.creditor = FakeUser(creditor_id)
        self.amount = amount


class FakeBalanceRepo:

    def __init__(self, balances):
        self._balances = balances

    def get_all(self):
        return self._balances


# ---------------------------------------------------------------------------
# Tests: get_all_expenses
# ---------------------------------------------------------------------------

def test_get_all_expenses_returns_list_of_dicts():

    expenses = [FakeExpense(1), FakeExpense(2)]
    service = ExpenseService(expense_model=FakeExpenseModel(expenses))

    result = service.get_all_expenses()

    assert isinstance(result, list)
    assert len(result) == 2


def test_get_all_expenses_maps_correct_fields():

    expenses = [FakeExpense(expense_id=5, payer_id=3, amount=200, split_type="EQUAL")]
    service = ExpenseService(expense_model=FakeExpenseModel(expenses))

    result = service.get_all_expenses()
    entry = result[0]

    assert entry["id"] == 5
    assert entry["payer_id"] == 3
    assert entry["amount"] == 200
    assert entry["split_type"] == "EQUAL"
    assert entry["created_at"] == "2026-01-01"


def test_get_all_expenses_includes_participant_ids():

    expense = FakeExpense(expense_id=1, payer_id=7)
    service = ExpenseService(expense_model=FakeExpenseModel([expense]))

    result = service.get_all_expenses()

    assert result[0]["participants"] == [7]


def test_get_all_expenses_returns_empty_list_when_no_expenses():

    service = ExpenseService(expense_model=FakeExpenseModel([]))

    result = service.get_all_expenses()

    assert result == []


# ---------------------------------------------------------------------------
# Tests: get_all_balances
# ---------------------------------------------------------------------------

def test_get_all_balances_filters_out_zero_amounts():

    balances = [FakeBalance(1, 2, 0), FakeBalance(3, 4, 50)]
    service = ExpenseService(balance_repo=FakeBalanceRepo(balances))

    result = service.get_all_balances()

    assert len(result) == 1
    assert result[0]["debtor_id"] == 3


def test_get_all_balances_filters_out_negative_amounts():

    balances = [FakeBalance(1, 2, -10), FakeBalance(3, 4, 20)]
    service = ExpenseService(balance_repo=FakeBalanceRepo(balances))

    result = service.get_all_balances()

    assert len(result) == 1
    assert result[0]["amount"] == 20


def test_get_all_balances_maps_correct_fields():

    balances = [FakeBalance(debtor_id=1, creditor_id=2, amount=75)]
    service = ExpenseService(balance_repo=FakeBalanceRepo(balances))

    result = service.get_all_balances()
    entry = result[0]

    assert entry["debtor_id"] == 1
    assert entry["creditor_id"] == 2
    assert entry["amount"] == 75


def test_get_all_balances_returns_empty_when_all_zero():

    balances = [FakeBalance(1, 2, 0), FakeBalance(3, 4, 0)]
    service = ExpenseService(balance_repo=FakeBalanceRepo(balances))

    result = service.get_all_balances()

    assert result == []
