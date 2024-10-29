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
            'stock': self.stock,
            'type': self.type,
            'weight': self.weight,
            'pricePerKilo': self.pricePerKilo,
            'quantity': self.quantity,
            'pricePerUnit': self.pricePerUnit,
            'pricePerPack': self.pricePerPack,
            'size': self.size
        }
    
    def __str__(self):
        return f'{self.name}'