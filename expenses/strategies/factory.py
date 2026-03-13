from .equal_split import EqualSplitStrategy


class StrategyFactory:

    @staticmethod
    def get_strategy(split_type):
        if split_type == "EQUAL":
            return EqualSplitStrategy()

        raise Exception("Invalid split type")