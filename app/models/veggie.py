from app import db
from .item import Item

class Veggie(db.Model):
    __tablename__ = 'veggie'
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    type = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_identity': 'veggie',
        'polymorphic_on': 'type'
    }

class WeightedVeggie(Veggie):
    __tablename__ = 'weightedVeggie'
    id = db.Column(db.Integer, db.ForeignKey('veggie.id'), primary_key=True)
    weight = db.Column(db.Numeric(precision=10, scale=2))
    pricePerKilo = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'weightedVeggie'
    }

class PackVeggie(Veggie):
    __tablename__ = 'packVeggie'
    id = db.Column(db.Integer, db.ForeignKey('veggie.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    pricePerPack = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'packVeggie'
    }

class UnitPriceVeggie(Veggie):
    __tablename__ = 'unitPriceVeggie'
    id = db.Column(db.Integer, db.ForeignKey('veggie.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    pricePerUnit = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'unitPriceVeggie'
    }