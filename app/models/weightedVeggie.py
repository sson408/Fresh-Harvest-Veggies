from app import db
from .veggie import Veggie

class WeightedVeggie(Veggie):
    __mapper_args__ = {
        'polymorphic_identity': 'weightedVeggie'
    }

    def __init__(self, name, weight=None, pricePerKilo=None):
        super().__init__(name)
        self.weight = weight
        self.pricePerKilo = pricePerKilo

    def __str__(self):
        return super().__str__() + f" {self.weight}kg"