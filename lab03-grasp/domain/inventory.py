from domain.inventory_item import InventoryItem

from domain.tax import TaxCalculatorFactory


class Inventory:
    def __init__(self):
        self.itens = []

    def add_new_item(self, name: str, price: float):
        tax_calculator = TaxCalculatorFactory.create(name)
        new_item = InventoryItem(name, price, tax_calculator)

        self.itens.append(new_item)

    def calculate_backback_value(self) -> float:
        total = 0.0

        for item in self.itens:
            total += item.calculate_price()

        return total
