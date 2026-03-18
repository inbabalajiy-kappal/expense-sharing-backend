import pytest

from expenses.services.factory.split_factory import SplitFactory
from expenses.services.strategies.equal_split import EqualSplitStrategy
from expenses.services.strategies.exact_split import ExactSplitStrategy
from expenses.services.strategies.percent_split import PercentSplitStrategy


def test_factory_returns_equal_strategy():

    assert isinstance(SplitFactory.create("EQUAL"), EqualSplitStrategy)


def test_factory_returns_exact_strategy():

    assert isinstance(SplitFactory.create("EXACT"), ExactSplitStrategy)


def test_factory_returns_percent_strategy():

    assert isinstance(SplitFactory.create("PERCENT"), PercentSplitStrategy)


def test_factory_raises_for_unknown_split_type():

    with pytest.raises(ValueError, match="Unsupported split type"):
        SplitFactory.create("UNKNOWN")