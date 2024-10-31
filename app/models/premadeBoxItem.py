from app import db

class PremadeBoxItem(db.Model):
    __tablename__ = 'premadeBoxItem'
    id = db.Column(db.Integer, primary_key=True)
    premadeBoxId = db.Column(db.Integer, db.ForeignKey('item.id'))
    itemId = db.Column(db.Integer, db.ForeignKey('item.id'))
    quantity = db.Column(db.Integer)

    premadeBox = db.relationship('PremadeBox', back_populates='premadeBoxItems', foreign_keys=[premadeBoxId])
    item = db.relationship('Item', back_populates='premadeBoxItems', foreign_keys=[itemId])

    def __init__(self, premadeBoxId, itemId, quantity):
        self.premadeBoxId = premadeBoxId
        self.itemId = itemId
        self.quantity = quantity

    def toDict(self):
        return {
            'id': self.id,
            'premadeBoxId': self.premadeBoxId,
            'itemId': self.itemId,
            'quantity': self.quantity
        }

    @classmethod
    def list(cls, filterWord):
        try:
            dataList = []
            if filterWord:
                premadeBoxItems = PremadeBoxItem.query.filter(PremadeBoxItem.name.ilike(f'%{filterWord}%')).all()
            else:
                premadeBoxItems = PremadeBoxItem.query.all()
            for premadeBoxItem in premadeBoxItems:
                dataList.append(premadeBoxItem.toDict())
            return dataList
        except Exception as e:
            return {'error': str(e)}

    def __str__(self):
        return super().__str__() + f" {self.quantity} units"