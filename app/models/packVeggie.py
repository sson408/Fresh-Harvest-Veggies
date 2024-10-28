from app import db
from .veggie import Veggie

class PackVeggie(Veggie):
    __tablename__ = 'packVeggie'
    id = db.Column(db.Integer, db.ForeignKey('veggie.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    pricePerPack = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'packVeggie'
    }