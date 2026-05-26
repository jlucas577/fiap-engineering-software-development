class PaymentApi:
    def charge(self, order_id, value):
        print(f"   [Payment API] Charging R$ {value} for order {order_id}... OK!")
        return {"status": "CHARGED"}

    def refund(self, order_id, value):
        print(
            f"   [Payment API] Processing REFUND of R$ {value} for order {order_id}... OK!"
        )
        return {"status": "REFUNDED"}
