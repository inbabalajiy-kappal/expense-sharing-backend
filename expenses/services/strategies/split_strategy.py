from abc import ABC, abstractmethod


class SplitStrategy(ABC):

    @abstractmethod
    def calculate(self, amount, participants):
        pass