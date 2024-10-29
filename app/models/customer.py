from app import db
from .person import Person

class Customer(Person):

    orders = db.relationship('Order', back_populates='customer')

    __mapper_args__ = {
        'polymorphic_identity': 3
    }

    def __init__(self, username, password, roleId, customerAddress, customerBalance, maxOwing):
        super().__init__(username, password, roleId)
        self.customerAddress = customerAddress
        self.customerBalance = customerBalance
        self.maxOwing = maxOwing

    def __str__(self):
        return f"customer: {self.id} {self.username}"