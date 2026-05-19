from taverna import TaverneiroService

from domain.inventory import Inventory


def test_venda_de_itens_simples():
    backpack = Inventory()
    service = TaverneiroService()

    service.sell_potion(backpack)
    service.sell_sword(backpack)

    # Valida se os itens entraram no inventario
    assert len(backpack.itens) == 2

    # Valida o cálculo total base
    total = service.calculate_backpack_value(backpack)
    assert total == 205.0  # 50.0 + 10% = 55.0 da Poção + 150.0 da Espada


def test_taxa_magica_desafio_final():
    backpack = Inventory()
    service = TaverneiroService()

    service.sell_potion(backpack)  # 50.0 + 10% = 55.0
    service.sell_sword(backpack)  # 150.0 (sem taxa)

    # O total deve ser 205.0 peças de ouro, mas o código legado não tem a taxa.
    total = service.calculate_backpack_value(backpack)

    assert total == 205.0, (
        "O desafio da Taxa Mágica (10% na Poção) ainda não foi implementado!"
    )
