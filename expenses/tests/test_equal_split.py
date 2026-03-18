from decimal import Decimal

import pytest

from expenses.services.strategies.equal_split import EqualSplitStrategy


class FakeUser:

    def __init__(self, user_id):
        self.id = user_id


def test_equal_split_divides_amount_evenly():

    strategy = EqualSplitStrategy()
    users = [FakeUser(1), FakeUser(2), FakeUser(3)]

    result = strategy.calculate(300, users)

    assert list(result.values()) == [Decimal("100.00"), Decimal("100.00"), Decimal("100.00")]


def test_equal_split_uses_participants_as_keys():

    strategy = EqualSplitStrategy()
    users = [FakeUser(1), FakeUser(2)]

    result = strategy.calculate(200, users)

    assert list(result.keys()) == users


def test_equal_split_rounds_to_two_decimal_places():

    strategy = EqualSplitStrategy()
    users = [FakeUser(1), FakeUser(2), FakeUser(3)]

    result = strategy.calculate(100, users)

    assert all(round(v, 2) == v for v in result.values())


def test_equal_split_single_participant_gets_full_amount():

    strategy = EqualSplitStrategy()
    users = [FakeUser(1)]

    result = strategy.calculate(150, users)

    assert list(result.values()) == [Decimal("150.00")]