# Class Buyer (Child of User)
from src.Domain.User.User import User


class Buyer(User):
    # Magic Method
    def __init__(self, user_id, email, password, name, user_type, money, repo):
        # Use parent class
        super().__init__(user_id, email, password, name, user_type, money, repo)
        # History
        self.__history = []
        self.__cart = []

if __name__ == "__main__":
    pass
