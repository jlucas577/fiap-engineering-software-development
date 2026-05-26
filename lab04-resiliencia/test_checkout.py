import pytest
import time
import responses
import requests as req_lib
 
from pytest_bdd import scenario, given, when, then, parsers
from checkout_service import CheckoutService


@responses.activate
@scenario("resiliencia.feature", "O Anti-Fraude está instável e deve falhar rápido")
def test_resiliencia_antifraude():
    pass


@pytest.fixture
def checkout():
    return CheckoutService(antifraud_url="http://api-antifraude/v1/validar")


@given("que o serviço de Anti-Fraude está com latência de 10s")
def setup_antifraude_lento():
    def request_callback(request):
        raise req_lib.exceptions.ReadTimeout("Simulated timeout")

    responses.add_callback(
        responses.GET,
        "http://api-antifraude/v1/validar",
        callback=request_callback,
        content_type="application/json",
    )


@when(
    parsers.parse('eu tento processar um pagamento de "{value}"'),
    target_fixture="result",
)
def process_payment(checkout, value):
    start_time = time.time()
    try:
        res = checkout.process_payment({"value": value})
        duration = time.time() - start_time
        return {"response": res, "duration": duration}
    except Exception as e:
        duration = time.time() - start_time
        return {"error": str(e), "duration": duration}


@then(parsers.parse("o sistema deve responder em menos de {limit:f}s"))
def validate_response_time(result, limit):
    assert result["duration"] < limit, f"Very slow system: {result['duration']}s"


@then(parsers.parse('deve retornar o status "{status}"'))
def validate_status(result, status):
    if "error" in result:
        pytest.fail(f"Unexpected error: {result['error']}")

    # Se o aluno não implementar o fallback, o status vindo do mock será "OK"
    # O teste espera "ANALISE_MANUAL" (que é o resultado do Fallback do Circuit Breaker)
    assert result["response"]["status"] == status
