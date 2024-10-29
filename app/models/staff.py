from app import db
from .person import Person

class Staff(Person):
    __mapper_args__ = {
        'polymorphic_identity': 2
    }

    def __init__(self, username, password, roleId, dateJoined, departmentId):
        super().__init__(username, password, roleId)
        self.dateJoined = dateJoined
        self.departmentId = departmentId

    def __str__(self):
        return f"staff: {self.id} {self.username}"