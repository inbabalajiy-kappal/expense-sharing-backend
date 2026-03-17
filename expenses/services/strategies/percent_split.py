from decimal import Decimal
from expenses.services.strategies.split_strategy import SplitStrategy


class PercentSplitStrategy(SplitStrategy):

    def calculate(self, amount, participants, metadata):
        return {
            user: Decimal(amount) * Decimal(percent) / 100
            for user, percent in zip(participants, metadata)
        }