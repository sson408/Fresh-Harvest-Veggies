from app import db
from .payment import Payment

class DebitCardPayment(Payment):
    __tablename__ = 'debitCardPayment'
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    bankName = db.Column(db.String(50))
    cardNumber = db.Column(db.String(16))
    cardExpirationDate = db.Column(db.Date)
    cvv = db.Column(db.String(3))
    
    __mapper_args__ = {
        'polymorphic_identity': 'debitCardPayment'
    }