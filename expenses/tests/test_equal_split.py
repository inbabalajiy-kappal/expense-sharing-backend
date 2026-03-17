from expenses.services.strategies.equal_split import EqualSplitStrategy


def test_equal_split():

    strategy = EqualSplitStrategy()

    result = strategy.calculate(300, [1, 2, 3])

    assert list(result.values()) == [100, 100, 100]