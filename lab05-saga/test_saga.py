import pytest

from pytest_bdd import scenario, given, when, then, parsers
from saga_service import OrquestradorSaga


@scenario("saga.feature", "Falha no estoque deve disparar estorno do pagamento")
def test_compensacao_saga():
    pass


@pytest.fixture
def orchestrator():
    return OrquestradorSaga()


@given(
    'que o cliente deseja realizar um pedido de valor "100.00"',
    target_fixture="order_data",
)
def setup_order():
    return {"order_id": "ORD-123", "value": 100.00, "product_id": "PROD-99"}


@when("o orquestrador tenta processar o pedido completo", target_fixture="result")
def process_order(orchestrator, order_data):
    try:
        res = orchestrator.process_complete_order(
            order_data["order_id"], order_data["value"], order_data["product_id"]
        )
        return res
    except Exception as e:
        return {"status": "UNHANDLED_ERROR", "msg": str(e)}


@then(parsers.parse('o status final deve ser "{expected_status}"'))
def validar_status_final(result, expected_status):
    assert result["status"] == expected_status, (
        f"Expected {expected_status} but got {result['status']}"
    )
