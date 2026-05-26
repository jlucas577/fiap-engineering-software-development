class StockApi:
    def book(self, order_id, product_id):
        print(
            f"   [Inventory API] Trying to reserve product #{product_id} for order #{order_id}... ERROR 500!"
        )
        raise Exception("Inventory Service Unavailable (Timeout)")
