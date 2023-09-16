# Class Seller (Child of User)
# It will later be child of Buyer
# It's because seller should also be able to buy
from src.Domain.User.User import User


class Seller(User):
    def __init__(self, user_id, email, password, name, money, user_type):
        super().__init__(user_id, email, password, name, money, user_type)


if __name__ == "__main__":
    pass
