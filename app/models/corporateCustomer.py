from app import db
from .customer import Customer

class CorporateCustomer(Customer):
    __mapper_args__ = {
        'polymorphic_identity': 4
    }

    def __init__(self, username, password, roleId, discountRate, maxCredit, minBalance):
        super().__init__(username, password, roleId)
        self.discountRate = discountRate
        self.maxCredit = maxCredit
        self.minBalance = minBalance

    def __str__(self):
        return f"corporateCustomer: {self.id} {self.username}"