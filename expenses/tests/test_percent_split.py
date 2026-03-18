from decimal import Decimal

from expenses.services.strategies.percent_split import PercentSplitStrategy


class FakeUser:

    def __init__(self, user_id):
        self.id = user_id


def test_percent_split_computes_shares_from_percentages():

    strategy = PercentSplitStrategy()
    users = [FakeUser(1), FakeUser(2)]

    result = strategy.calculate(200, users, metadata=[70, 30])

    assert result[users[0]] == Decimal("140.00")
    assert result[users[1]] == Decimal("60.00")


def test_percent_split_uses_participants_as_keys():

    strategy = PercentSplitStrategy()
    users = [FakeUser(1), FakeUser(2)]

    result = strategy.calculate(100, users, metadata=[50, 50])

    assert list(result.keys()) == users


def test_percent_split_single_participant_at_100_percent():

    strategy = PercentSplitStrategy()
    users = [FakeUser(1)]

    result = strategy.calculate(250, users, metadata=[100])

    assert result[users[0]] == Decimal("250.00")
