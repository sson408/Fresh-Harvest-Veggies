from flask import jsonify
from app import db
from .item import Item

class PremadeBox(Item):
    __mapper_args__ = {
        'polymorphic_identity': 'premade_box', 
    }

    premadeBoxItems = db.relationship('PremadeBoxItem', back_populates='premadeBox', foreign_keys='PremadeBoxItem.premadeBoxId', cascade='all, delete-orphan')
    def __init__(self, name, size=None, quantity=None, price=None):
        super().__init__(name)
        self.size = size
        self.quantity = quantity
        self.price = price

    def toDict(self):
        # convert the premadeBoxItems to a list of dictionaries
        box_dict = super().toDict()
        box_dict['items'] = [{'item': item.item.toDict(), 'quantity': item.quantity} for item in self.premadeBoxItems]
        return box_dict

    @classmethod
    def listAllPremadeBoxes(cls):
        try:
            dataList = cls.query.filter(Item.type == 'premade_box').all()

            return jsonify({"premadeBoxes": [data.toDict() for data in dataList]}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def __str__(self):
        return super().__str__() + f" {self.size} units"