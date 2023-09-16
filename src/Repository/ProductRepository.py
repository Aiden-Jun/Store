from src.Domain.Product import Product
from src.Repository.BaseRepository import BaseRepository


class ProductRepository(BaseRepository):

    def find_products_by_buyer_id(self, buyer_id):
        buyer_id = str(buyer_id)
        product_rows = self._db.read("products.csv")
        products = []
        for product_row in product_rows:
            if product_row[6] == buyer_id:
                products.append(self.convert_product_from_row_to_object(product_row))
        return products

    def find_selling_products(self):
        product_rows = self._db.read("products.csv")
        products = []
        for product_row in product_rows:
            if product_row[4] == "1":
                products.append(self.convert_product_from_row_to_object(product_row))
        return products

    def find_product_using_id(self, product_id):
        product_id = str(product_id)
        product_rows = self._db.read("products.csv")
        for product_row in product_rows:
            print(product_row)
            print(product_id)
            if product_row[0] == product_id:
                return self.convert_product_from_row_to_object(product_row)
        return None

    @staticmethod
    def convert_product_from_row_to_object(pr):
        return Product(pr[0], pr[1], pr[2], pr[3], pr[4], pr[5], pr[6])
