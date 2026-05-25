from repository.order_repository import OrderRepository

from service.notification_service import NotificationService

from domain.discount import VipDiscount
from domain.discount import PremiumDiscount
from domain.discount import DefaultDiscount

from domain.shipping import NortheastShipping
from domain.shipping import NorthShipping
from domain.shipping import SouthShipping
from domain.shipping import DefaultShipping


class ThunderMegazord:
    def process_central_command(self, orderData: dict) -> bool:
        print("--- INICIANDO PROTOCOLO MEGAZORD ---")

        orderRepository = OrderRepository()
        notificationService = NotificationService()

        # 1. Sensores de Validação
        if not orderData.get("itens"):
            print("[ALERTA] Sistema sem munição (pedido sem itens)")
            return False

        # 2. Núcleo de Desconto
        finalValue = orderData.get("valor_total", 0.0)
        clientType = orderData.get("tipo_cliente", "comum")

        discountStrategies = {
            "vip": VipDiscount(),
            "premium": PremiumDiscount(),
            "default": DefaultDiscount(),
        }

        currentDiscountStrategy = discountStrategies.get(clientType, DefaultDiscount())
        finalValue = currentDiscountStrategy.calc(finalValue)

        # 3. Propulsores de Frete
        shippingStrategies = {
            "north": NorthShipping(),
            "northeast": NortheastShipping(),
            "south": SouthShipping(),
        }

        region = orderData.get("regiao", "south")
        currentShippingStrategy = shippingStrategies.get(region, DefaultShipping())
        shippingValue = currentShippingStrategy.calc()

        finalValue = finalValue + shippingValue

        # 4. Memória de Armazenamento
        orderRepository.save(finalValue)

        # 5. Comunicação Intergaláctica
        notificationService.notify(orderData.get("email"))

        print("--- OPERAÇÃO MEGAZORD CONCLUÍDA ---")
        return True


if __name__ == "__main__":
    megazord = ThunderMegazord()
    mission = {
        "itens": ["Espada Thunder", "Escudo"],
        "valor_total": 5000.0,
        "tipo_cliente": "vip",
        "regiao": "north",
        "email": "zordon@alameda.com",
    }
    megazord.process_central_command(mission)
