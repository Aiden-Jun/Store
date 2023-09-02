from src.Domain.User.Buyer import Buyer
from src.Domain.User.Seller import Seller
from src.Domain.User.User import User
from src.Infrastructure.Database import Database


class Repository(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__db = Database()

    def find_user_by_email(self, email):
        user_rows = self.__db.read("users.csv")
        for user_row in user_rows:
            if user_row[0] == email:
                return user_row
        return None

    def find_user_by_email_and_password(self, email, password):
        user_rows = self.__db.read("users.csv")
        for user_row in user_rows:
            if user_row[0] == email:
                return self.convert_user_from_row_to_object(user_row)
        return None

    def add_user(self, email, password, name, user_type):
        self.__db.write("users.csv", [email, password, name, user_type, 0])

    def convert_user_from_row_to_object(self, user_row):
        if user_row[3] == 'seller':
            return Seller(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5])
        else:
            return Buyer(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5])

    def find_products_by_buyer_id(self, buyer_id):
        product_rows = self.__db.read("products.csv")
        products = []
        for product_row in product_rows:
            if product_row[6] == buyer_id:
                products.append(self.convert_product_from_row_to_object(product_row))
        return products

    def find_selling_products(self):
        product_rows = self.__db.read("products.csv")
        products = []
        for product_row in product_rows:
            if product_row[4] == "1":
                products.append(self.convert_product_from_row_to_object(product_row))
        return products
