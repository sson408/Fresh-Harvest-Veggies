from app import db
from .item import Item

class Veggie(Item):
   
    __mapper_args__ = {
        'polymorphic_identity': 'veggie',
    }

    def __init__(self, name):
        super().__init__(name, )
        self.type = 'veggie'  
        self.name = name
  

    def __str__(self):
        return f"{self.name}"




