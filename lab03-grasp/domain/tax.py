from abc import ABC, abstractmethod


class TaxCalculatorFactory:
    @staticmethod
    def create(name: str):
        if name.lower().startswith("poção"):
            return MagicItemTax()

        return NoTax()


class TaxCalculator(ABC):
    @abstractmethod
    def calc(self, price: float) -> float:
        pass


class MagicItemTax(TaxCalculator):
    def calc(self, price: float) -> float:
        return price * 1.10


class NoTax(TaxCalculator):
    def calc(self, price: float) -> float:
        return price
