from app import db

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    orderDate = db.Column(db.Date)
    orderStatus = db.Column(db.String(20))
    orderTotal = db.Column(db.Float)
    customerId = db.Column(db.Integer, db.ForeignKey('person.id'))
    
    customer = db.relationship('Customer', back_populates='orders', foreign_keys=[customerId])

    orderLines = db.relationship('OrderLine', back_populates='order')