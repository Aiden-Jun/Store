from src.Domain.User.Buyer import Buyer
from src.Domain.User.Seller import Seller
from src.Domain.User.User import User
from src.Infrastructure.Database import Database
from src.Repository.UserRepository import UserRepository


class Repository(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_repository(self):
        return self.user_repository
