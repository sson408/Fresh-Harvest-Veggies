from app import db
from .veggie import Veggie

class PackVeggie(Veggie):

    __mapper_args__ = {
        'polymorphic_identity': 'packVeggie'
    }

    def __init__(self, name, quantity=None, pricePerPack=None):
        super().__init__(name)
        self.quantity = quantity
        self.pricePerPack = pricePerPack

    def __str__(self):
        return super().__str__() + f" {self.quantity} packs"