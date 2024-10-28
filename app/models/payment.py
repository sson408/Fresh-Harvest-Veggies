from app import db

class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    paymentMethodId = db.Column(db.Integer)
    paymentDate = db.Column(db.Date)
    paymentAmount = db.Column(db.Float)
    
    __mapper_args__ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'paymentMethodId'
    }