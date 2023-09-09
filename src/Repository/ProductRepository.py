from src.Domain.User.Buyer import Buyer
from src.Domain.User.Seller import Seller
from src.Domain.User.User import User
from src.Infrastructure.Database import Database
from src.Domain.Product import Product

class ProductRepository(object):

    def __init__(self):
        self.__db = Database()

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

    def convert_product_from_row_to_object(self, pr):
        return Product(pr[0],pr[1],pr[2],pr[3],pr[4],pr[5],pr[6])