from Service.AuthService import AuthService
from Service.ProductService import ProductService
from Service.UserService import UserService
from Service.UiService import UiService

class Service(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__auth_service = AuthService()
        self.__user_service = UserService()
        self.__product_service = ProductService()
        self.__ui_service = UiService()

    def get_auth_service(self):
        return self.__auth_service

    def get_user_service(self):
        return self.__user_service

    def get_product_service(self):
        return self.__product_service
    
    def get_ui_service(self):
        return self.__ui_service