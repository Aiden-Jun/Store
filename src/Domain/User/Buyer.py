# Class Buyer (Child of User)
from src.Domain.User.User import User


class Buyer(User):
    # Magic Method
    def __init__(self, user_id, email, password, name, money, user_type):
        super().__init__(user_id, email, password, name, money, user_type)


if __name__ == "__main__":
    pass
