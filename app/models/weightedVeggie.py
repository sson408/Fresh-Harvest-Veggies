from app import db
from .veggie import Veggie

class WeightedVeggie(Veggie):
    __tablename__ = 'weightedVeggie'
    id = db.Column(db.Integer, db.ForeignKey('veggie.id'), primary_key=True)
    weight = db.Column(db.Numeric(precision=10, scale=2))
    pricePerKilo = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'weightedVeggie'
    }