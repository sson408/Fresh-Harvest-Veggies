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





