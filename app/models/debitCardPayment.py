from app import db
from .payment import Payment

class DebitCardPayment(Payment):
    __mapper_args__ = {
        'polymorphic_identity': 'debitCardPayment'
    }

    def __init__(self, paymentMethodId, paymentDate, paymentAmount, bankName, cardNumber, cardExpirationDate, cvv):
        super().__init__(paymentMethodId, paymentDate, paymentAmount)
        self.bankName = bankName
        self.cardNumber = cardNumber
        self.cardExpirationDate = cardExpirationDate
        self.cvv = cvv

    def __str__(self):
        return f'DebitCardPayment: {self.id}'