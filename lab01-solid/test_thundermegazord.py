from thundermegazord import ThunderMegazord


def test_process_order_successfully():
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "south",
        "email": "teste@teste.com",
    }

    assert megazord.process_central_command(mission) is True


def test_process_order_fails_when_items_are_empty():
    megazord = ThunderMegazord()
    mission = {
        "itens": [],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "south",
        "email": "teste@teste.com",
    }

    assert megazord.process_central_command(mission) is False


def test_calculates_final_value_for_vip_customer_from_north(capsys):
    # VIP: 50% de desconto (100 -> 50)
    # North: 50 de frete (50 + 50 = 100)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "north",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 100.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_vip_customer_from_northeast(capsys):
    # VIP: 50% de desconto (100 -> 50)
    # Northeast: 40 de frete (50 + 40 = 90)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "northeast",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 90.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_vip_customer_from_south(capsys):
    # VIP: 50% de desconto (100 -> 50)
    # South: 30 de frete (50 + 30 = 80)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "south",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 80.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_vip_customer_with_default_shipping(capsys):
    # VIP: 50% de desconto (100 -> 50)
    # Default: 20 de frete (50 + 20 = 70)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "vip",
        "regiao": "default",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 70.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_premium_customer_from_north(capsys):
    # Premium: 10% de desconto (100 -> 90)
    # North: 50 de frete (90 + 50 = 140)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "premium",
        "regiao": "north",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 140.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_premium_customer_from_northeast(capsys):
    # Premium: 10% de desconto (100 -> 90)
    # Northeast: 40 de frete (90 + 40 = 130)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "premium",
        "regiao": "northeast",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 130.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_premium_customer_from_south(capsys):
    # Premium: 10% de desconto (100 -> 90)
    # South: 30 de frete (90 + 30 = 120)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "premium",
        "regiao": "south",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 120.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_premium_customer_with_default_shipping(capsys):
    # Premium: 10% de desconto (100 -> 90)
    # Default: 20 de frete (90 + 20 = 110)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "premium",
        "regiao": "default",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 110.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_default_customer_from_north(capsys):
    # Default: 5% de desconto (100 -> 95)
    # North: 50 de frete (95 + 50 = 145)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "default",
        "regiao": "north",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 145.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_default_customer_from_northeast(capsys):
    # Default: 5% de desconto (100 -> 95)
    # Northeast: 40 de frete (95 + 40 = 135)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "default",
        "regiao": "northeast",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 135.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_default_customer_from_south(capsys):
    # Default: 5% de desconto (100 -> 95)
    # South: 30 de frete (95 + 30 = 125)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "default",
        "regiao": "south",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 125.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_default_customer_with_default_shipping(capsys):
    # Default: 5% de desconto (100 -> 95)
    # Default: 20 de frete (95 + 20 = 115)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "default",
        "regiao": "default",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 115.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"


def test_calculates_final_value_for_invalid_client_type_and_region(capsys):
    # Default: 5% de desconto (100 -> 95)
    # Default: 20 de frete (95 + 20 = 115)
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Item 1"],
        "valor_total": 100.0,
        "tipo_cliente": "premier",
        "regiao": "centar",
    }

    response = megazord.process_central_command(mission)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert response is True

    assert lines[0] == "--- INICIANDO PROTOCOLO MEGAZORD ---"
    assert any("[LOG] Gravando dados no cristal de memória" in line for line in lines)
    assert "[STATUS] Energia Final Requerida: R$ 115.00" in lines
    assert lines[-1] == "--- OPERAÇÃO MEGAZORD CONCLUÍDA ---"
