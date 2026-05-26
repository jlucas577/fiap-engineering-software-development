import requests

from tenacity import retry, stop_after_attempt, wait_fixed


def secure_fallback(retry_state):
    print("!!! WARNING: Unstable anti-fraud system, triggering security fallback !!!")
    return {
        "status": "ANALISE_MANUAL",
        "code": 202,
        "message": "Payment received. Please wait for manual review due to technical instability.",
    }


class CheckoutService:
    def __init__(self, antifraud_url="http://localhost:8080/v1/validar"):
        self.antifraud_url = antifraud_url

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(0.1),
        retry_error_callback=secure_fallback,
    )
    def process_payment(self, transaction):
        response = requests.get(self.antifraud_url, timeout=0.5)
        return response.json()
