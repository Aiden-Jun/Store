from src.Domain.User.Buyer import Buyer
from src.Domain.User.Seller import Seller
from src.Domain.User.User import User
from src.Infrastructure.Database import Database
from src.Repository.UserRepository import UserRepository
from src.Repository.ProductRepository import ProductRepository

class Repository(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.user_repository = UserRepository()
        self.product_repository = ProductRepository()

    def get_user_repository(self):
        print('Getting user repo')
        return self.user_repository

    def get_product_repository(self):
        print('Getting product repo')
        return self.product_repository