import uuid


class OrderRepository:
    def save(self, finalValue: float):
        orderId = str(uuid.uuid4())[:8]

        print(f"[LOG] Gravando dados no cristal de memória {orderId}...")
        print(f"[STATUS] Energia Final Requerida: R$ {finalValue:.2f}")
