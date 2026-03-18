from decimal import Decimal

import pytest

from expenses.services.strategies.exact_split import ExactSplitStrategy


class FakeUser:

    def __init__(self, user_id):
        self.id = user_id


def test_exact_split_assigns_specified_shares():

    strategy = ExactSplitStrategy()
    users = [FakeUser(1), FakeUser(2)]

    result = strategy.calculate(300, users, metadata=[200, 100])

    assert list(result.values()) == [200, 100]


def test_exact_split_uses_participants_as_keys():

    strategy = ExactSplitStrategy()
    users = [FakeUser(1), FakeUser(2)]

    result = strategy.calculate(300, users, metadata=[200, 100])

    assert list(result.keys()) == users


def test_exact_split_single_participant():

    strategy = ExactSplitStrategy()
    users = [FakeUser(1)]

    result = strategy.calculate(100, users, metadata=[100])

    assert list(result.values()) == [100]
