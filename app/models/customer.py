from app import db
from .person import Person

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True) 
    customerAddress = db.Column(db.String(500))
    customerBalance = db.Column(db.Numeric(precision=10, scale=2))
    maxOwing = db.Column(db.Numeric(precision=10, scale=2))

    orders = db.relationship('Order', back_populates='customer')

    __mapper_args__ = {
        'polymorphic_identity': 3
    }