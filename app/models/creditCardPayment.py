from app import db
from .payment import Payment

class CreditCardPayment(Payment):
    __tablename__ = 'creditCardPayment'
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    cardNumber = db.Column(db.String(16))
    cardType = db.Column(db.String(10))
    cardExpirationDate = db.Column(db.Date)
    cvv = db.Column(db.String(3))
    
    __mapper_args__ = {
        'polymorphic_identity': 'creditCardPayment'
    }