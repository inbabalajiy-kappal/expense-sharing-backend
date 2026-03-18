from expenses.services.strategies.equal_split import EqualSplitStrategy
from expenses.services.strategies.exact_split import ExactSplitStrategy
from expenses.services.strategies.percent_split import PercentSplitStrategy


class SplitFactory:

    _types = {
        "EQUAL": EqualSplitStrategy,
        "EXACT": ExactSplitStrategy,
        "PERCENT": PercentSplitStrategy,
    }

    @classmethod
    def create(cls, split_type):
        try:
            return cls._types[split_type]()
        except KeyError as exc:
            raise ValueError(f"Unsupported split type: {split_type}") from exc


SplitStrategyFactory = SplitFactory