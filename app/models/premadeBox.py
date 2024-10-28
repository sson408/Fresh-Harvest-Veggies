from app import db
from .item import Item

class PremadeBox(db.Model):
    __tablename__ = 'premadeBoxes'
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    size = db.Column(db.Integer)  
    quantity = db.Column(db.Integer)
    price = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 'premade_box', 
    }