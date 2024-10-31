from operator import or_
from flask import jsonify
from app import db
from .person import Person
from .enum import userRole, department

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

    def toDict(self):
        return super().toDict()
    
    @classmethod
    def list(cls, filterWord):
        # filter by username, firstname, lastname, email, phone number, department name, address
        try:
            dataList = []
            if filterWord:
                word = filterWord.lower()
                dataList = cls.query.filter(
                    or_(Customer.roleId == 3 , Customer.roleId == 4) & (
                        Customer.username.like(f'%{word}%') |
                        Customer.firstName.like(f'%{word}%') |
                        Customer.lastName.like(f'%{word}%') |
                        Customer.email.like(f'%{word}%') |
                        Customer.phoneNumber.like(f'%{word}%') |
                        Customer.customerAddress.like(f'%{word}%')
                    )
                ).all()
            else:
                dataList = cls.query.filter(or_(Customer.roleId == 3, Customer.roleId == 4)).all()


            return jsonify({"customers": [data.toDict() for data in dataList]}), 200
        except Exception as e:
            print(e)
            return jsonify({'message': 'An error occurred: ' + str(e)}), 500
    
    def __str__(self):
        return f"customer: {self.id} {self.username}"