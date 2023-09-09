from src.Repository.Repository import Repository


class ProductService(object):
    def __init__(self):
        self.__all_products = {}
        self.__repository = Repository()

    def get_buy_products(self, user_id):
        products = self.__repository.get_product_repository().find_products_by_buyer_id(user_id)
        products_dto = []
        for product in products:
            products_dto.append(product.convert_dto())
        return products_dto

    def get_selling_products(self):
        products = self.__repository.get_product_repository().find_selling_products()
        products_dto = []
        for product in products:
            products_dto.append(product.convert_dto())
        return products_dto

    def get_products_list_of_user_id(self, user_id):
        return self.__all_products[user_id]

    def get_all_seller_and_products(self):
        return self.__all_products

    def get_product_object(self, seller_id, product_index):
        return self.__all_products[seller_id][product_index]

    def add_product(self, seller_id, product):
        self.__all_products[seller_id].append(product)

    def delete_product(self, seller_id, product_index):
        self.__all_products[seller_id].pop(product_index)
