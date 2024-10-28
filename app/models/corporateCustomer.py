from app import db
from .customer import Customer

class CorporateCustomer(Customer):
    __tablename__ = 'corporateCustomer'
    id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    discountRate = db.Column(db.Numeric(precision=10, scale=2))
    maxCredit = db.Column(db.Numeric(precision=10, scale=2))
    minBalance = db.Column(db.Numeric(precision=10, scale=2))

    __mapper_args__ = {
        'polymorphic_identity': 4
    }