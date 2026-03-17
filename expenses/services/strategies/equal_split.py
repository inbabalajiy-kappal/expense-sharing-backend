from decimal import Decimal
from expenses.services.strategies.split_strategy import SplitStrategy


class EqualSplitStrategy(SplitStrategy):

    def calculate(self, amount, participants, metadata=None):
        share = round(Decimal(amount) / len(participants), 2)

        return dict(
            zip(
                participants,
                [share] * len(participants)
            )
        )