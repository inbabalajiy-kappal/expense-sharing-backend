from expenses.services.factory.split_factory import SplitFactory


def test_factory():

    strategy = SplitFactory.create("EQUAL")

    assert strategy.__class__.__name__ == "EqualSplitStrategy"