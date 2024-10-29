from app import db
from .payment import Payment

class CreditCardPayment(Payment):
    __mapper_args__ = {
        'polymorphic_identity': 'creditCardPayment'
    }

    def __init__(self, paymentMethodId, paymentDate, paymentAmount, cardNumber = None, cardType = None, cardExpirationDate = None, cvv = None):
        super().__init__(paymentMethodId, paymentDate, paymentAmount)
        self.cardNumber = cardNumber
        self.cardType = cardType
        self.cardExpirationDate = cardExpirationDate
        self.cvv = cvv

    def __str__(self):
        return f'CreditCardPayment: {self.id}'