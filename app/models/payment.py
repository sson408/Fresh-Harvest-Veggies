from app import db
from .enum import paymentMethod

class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    paymentMethodId = db.Column(db.Integer)
    paymentDate = db.Column(db.Date)
    paymentAmount = db.Column(db.Float)
    cardNumber = db.Column(db.String(16))
    cardType = db.Column(db.String(10))
    cardExpirationDate = db.Column(db.Date)
    cvv = db.Column(db.String(3))
    bankName = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'paymentMethodId'
    }

    def __init__(self, paymentMethodId, paymentDate, paymentAmount, cardNumber = None, cardType = None, cardExpirationDate = None, cvv = None, bankName = None):
        self.paymentMethodId = paymentMethodId
        self.paymentMethod = paymentMethod(paymentMethodId).name if paymentMethodId else ""
        self.paymentDate = paymentDate
        self.paymentDateDisplay = paymentDate.strftime('%Y-%m-%d') if paymentDate else ""
        self.paymentAmount = paymentAmount
        self.cardNumber = cardNumber
        self.cardType = cardType
        self.cardExpirationDate = cardExpirationDate
        self.cvv = cvv
        self.bankName = bankName
  

    def toDict(self):
        return {
            'id': self.id,
            'paymentMethodId': self.paymentMethodId,
            'paymentMethod': paymentMethod(self.paymentMethodId).name if self.paymentMethodId else "",
            'paymentDate': self.paymentDate.strftime('%Y-%m-%d') if self.paymentDate else "",
            'paymentAmount': self.paymentAmount,
            'cardNumber': self.cardNumber,
            'cardType': self.cardType,
            'cardExpirationDate': self.cardExpirationDate.strftime('%Y-%m-%d') if self.cardExpirationDate else "",
            'cvv': self.cvv,
            'bankName': self.bankName        
        }
    
    def __str__(self):
        return f'Payment: {self.id}'