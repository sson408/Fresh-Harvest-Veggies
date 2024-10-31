from operator import not_
from flask import jsonify
from app import db

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    type = db.Column(db.String(50))
    weight = db.Column(db.Numeric(precision=10, scale=2))
    pricePerKilo = db.Column(db.Numeric(precision=10, scale=2))
    quantity = db.Column(db.Integer)
    pricePerUnit = db.Column(db.Numeric(precision=10, scale=2))
    pricePerPack = db.Column(db.Numeric(precision=10, scale=2))
    size = db.Column(db.Integer)  

    __mapper_args__ = {
        'polymorphic_identity': 'item', 
        'polymorphic_on': 'type'        
    }

    orderLines = db.relationship('OrderLine', back_populates='item')
    premadeBoxItems = db.relationship('PremadeBoxItem', back_populates='item', foreign_keys='PremadeBoxItem.itemId')


    def __init__(self, name, price = None, stock = None, type = None, weight=None, pricePerKilo=None, quantity=None, pricePerUnit=None, pricePerPack=None, size=None):
        self.name = name
        self.price = price
        self.stock = stock
        self.type = type
        self.weight = weight
        self.pricePerKilo = pricePerKilo
        self.quantity = quantity
        self.pricePerUnit = pricePerUnit
        self.pricePerPack = pricePerPack
        self.size = size


    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'priceDisplay': f'${self.price:.2f}' if self.price else "",
            'stock': self.stock,
            'type': self.type,
            'weight': self.weight,
            'pricePerKilo': self.pricePerKilo,
            'pricePerKiloDisplay': f'${self.pricePerKilo:.2f}' if self.pricePerKilo else "",
            'quantity': self.quantity,
            'pricePerUnit': self.pricePerUnit,
            'pricePerUnitDisplay': f'${self.pricePerUnit:.2f}' if self.pricePerUnit else "",
            'pricePerPack': self.pricePerPack,
            'pricePerPackDisplay': f'${self.pricePerPack:.2f}' if self.pricePerPack else "",
            'size': self.size
        }
    
    @classmethod
    def listAllVeges(cls, filterWord):
        try:
            dataList = []
            if filterWord:
                word = filterWord.lower()
                dataList = cls.query.filter(
                    cls.name.like(f'%{word}%')
                ).filter(Item.type != 'premade_box').all()
            else:
                dataList = cls.query.filter(Item.type != 'premade_box').all()

            return jsonify({"items": [data.toDict() for data in dataList]}), 200
        except Exception as e:
            print(e)
            return jsonify({'message': 'An error occurred: ' + str(e)}), 500

    def __str__(self):
        return f'{self.name}'