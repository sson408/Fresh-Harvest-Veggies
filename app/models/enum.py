from enum import Enum

class userRole(Enum):
    administrator = 1
    staff = 2
    customer = 3
    corporate_customer = 4


class department(Enum):
    admin = 1
    user = 2


class paymentMethod(Enum):
    creditCard = 1
    debitCard = 2