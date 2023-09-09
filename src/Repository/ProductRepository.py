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

    def find_product_using_id(self, product_id):
        product_rows = self.__db.read("products.csv")
        for product_row in product_rows:
            print(product_row)
            print(product_id)
            if product_row[0] == product_id:
                return self.convert_product_from_row_to_object(product_row)
        return None
    
    def update_product_selling_status(self, product_id, buyer_id, new_status):
        product_rows = self.__db.read("products.csv")
        for product_row in product_rows:
            if product_row[0] == product_id:
                product_row[4] = new_status
                product_row[6] = buyer_id
                self.__db.write('products.csv', product_row)
                return


    def convert_product_from_row_to_object(self, pr):
        return Product(pr[0],pr[1],pr[2],pr[3],pr[4],pr[5],pr[6])
    
    def buy_product_with_buyer_id(self, product_id, buyer_id):
        self.__db