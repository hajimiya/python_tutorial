from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by card"

payment = CardPayment()
print(payment.pay(500))
