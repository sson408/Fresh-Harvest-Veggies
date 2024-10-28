from app import db

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'item', 
        'polymorphic_on': 'type'        
    }

    orderLines = db.relationship('OrderLine', back_populates='item')