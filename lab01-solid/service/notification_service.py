class NotificationService:
    def notify(self, email: str):
        if email:
            print(f"[SINAL] Enviando telemetria para {email}...")
