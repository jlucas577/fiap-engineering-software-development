from payment_api import PaymentApi
from stock_api import StockApi


class OrquestradorSaga:
    def __init__(self):
        self.payment_api = PaymentApi()
        self.stock_api = StockApi()

    def process_complete_order(self, order_id, value, product_id):
        print(f"\n[SAGA] Order processing initiated: {order_id}")

        self.payment_api.charge(order_id, value)

        try:
            self.stock_api.book(order_id, product_id)
            return {"status": "SUCCESS"}
        except Exception as e:
            print(f"\n[SAGA] Critical stock failure detected: {e}")

            response_refund = self.payment_api.refund(order_id, value)

            if response_refund["status"] == "REFUNDED":
                return {
                    "status": "CANCELLED_WITH_REFUND",
                    "reason": "Insufficient stock",
                }
            else:
                return {
                    "status": "CRITICAL_FAILURE",
                    "reason": "Failed to process the refund",
                }
