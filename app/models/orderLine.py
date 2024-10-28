from app import db

class OrderLine(db.Model):
    __tablename__ = 'orderLine'
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'))
    itemId = db.Column(db.Integer, db.ForeignKey('item.id'))
    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Numeric(precision=10, scale=2))

    order = db.relationship('Order', back_populates='orderLines')
    item = db.relationship('Item', back_populates='orderLines')