from expenses.services.strategies.split_strategy import SplitStrategy


class ExactSplitStrategy(SplitStrategy):

    def calculate(self, amount, participants, metadata):
        return dict(
            zip(participants, metadata)
        )