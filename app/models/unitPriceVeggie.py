from app import db
from .veggie import Veggie

class UnitPriceVeggie(Veggie):

    __mapper_args__ = {
        'polymorphic_identity': 'unitPriceVeggie'
    }

    def __init__(self, name, quantity=None, pricePerUnit=None):
        super().__init__(name)
        self.quantity = quantity
        self.pricePerUnit = pricePerUnit

    def __str__(self):
        return super().__str__() + f" {self.quantity} units"