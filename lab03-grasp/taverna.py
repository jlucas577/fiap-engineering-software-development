from domain.inventory import Inventory


class TaverneiroService:
    """
    O PROBLEMA: Faz todo o trabalho, violando Information Expert e Creator.
    """

    def sell_potion(self, inventory: Inventory):
        print("Taverneiro: 'Aqui está sua poção, forasteiro!'")
        inventory.add_new_item("Poção de Cura", 50.0)

    def sell_sword(self, inventory: Inventory):
        print("Taverneiro: 'Esta é uma lâmina afiada!'")
        inventory.add_new_item("Espada Longa", 150.0)

    def calculate_backpack_value(self, inventory: Inventory) -> float:
        return inventory.calculate_backback_value()


if __name__ == "__main__":
    backback = Inventory()
    service = TaverneiroService()

    service.sell_potion(backback)
    service.sell_sword(backback)

    value = service.calculate_backpack_value(backback)

    print(f"O valor total devido é de: {value} peças de ouro.")
