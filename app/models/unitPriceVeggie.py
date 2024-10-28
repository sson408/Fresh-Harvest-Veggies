from app import db
from .veggie import Veggie

class UnitPriceVeggie(Veggie):
    __tablename__ = 'unitPriceVeggie'
    id = db.Column(db.Integer, db.ForeignKey('veggie.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    pricePerUnit = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'unitPriceVeggie'
    }