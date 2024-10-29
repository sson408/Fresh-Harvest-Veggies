from app import db
from .item import Item

class PremadeBox(Item):
    __mapper_args__ = {
        'polymorphic_identity': 'premade_box', 
    }

    def __init__(self, name, size=None, quantity=None, price=None):
        super().__init__(name)
        self.size = size
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return super().__str__() + f" {self.size} units"