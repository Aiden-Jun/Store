from src.Repository.UserRepository import UserRepository
from src.Repository.ProductRepository import ProductRepository


class Repository(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.user_repository = UserRepository('users.csv')
        self.product_repository = ProductRepository('products.csv')

    def user(self):
        print('Getting user repo')
        return self.user_repository

    def product(self):
        print('Getting product repo')
        return self.product_repository
