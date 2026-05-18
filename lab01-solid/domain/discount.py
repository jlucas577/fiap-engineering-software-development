from abc import ABC, abstractmethod


class DiscountCalculator(ABC):
    @abstractmethod
    def calc(self, value: float) -> float:
        pass


class VipDiscount(DiscountCalculator):
    def calc(self, value: float) -> float:
        return value * 0.5


class PremiumDiscount(DiscountCalculator):
    def calc(self, value: float) -> float:
        return value * 0.9


class DefaultDiscount(DiscountCalculator):
    def calc(self, value: float) -> float:
        return value * 0.95
