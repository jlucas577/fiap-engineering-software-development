from domain.tax import TaxCalculator


class InventoryItem:
    def __init__(self, name: str, price: float, tax_calculator: TaxCalculator):
        self.name = name
        self.price = price
        self.tax_calculator = tax_calculator

    def calculate_price(self):
        return self.tax_calculator.calc(self.price)
