from abc import ABC, abstractmethod


class ShippingCalculator(ABC):
    @abstractmethod
    def calc(self) -> float:
        pass


class NorthShipping(ShippingCalculator):
    def calc(self) -> float:
        return 50.0


class NortheastShipping(ShippingCalculator):
    def calc(self) -> float:
        return 40.0


class SouthShipping(ShippingCalculator):
    def calc(self) -> float:
        return 30.0


class DefaultShipping(ShippingCalculator):
    def calc(self) -> float:
        return 20.0
