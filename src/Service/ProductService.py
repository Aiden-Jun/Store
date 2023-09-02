from src.Repository.Repository import Repository


class ProductService(object):
    def __init__(self):
        self.__all_products = {}
        self.__repository = Repository()

    def get_buy_products(self, user_id):
        products = self.__repository.find_products_by_buyer_id(user_id)
        productsDTO = []
        for product in products:
            productsDTO.append({
                'product_id': product.get_product_id(),
                'product_name': product.get_product_name(),
                'description': product.get_product_description(),
                'product_price': product.get_product_price(),
                'is_selling': product.get_product_id(),
                'seller_id': product.get_product_seller_id(),
                'buyer_id': product.get_product_id,
            })
        return productsDTO
    def get_selling_products(self):
        products = self.__repository.find_selling_products()
        productsDTO = []
        for product in products:
            productsDTO.append({
                'product_id': product.get_product_id(),
                'product_name': product.get_product_name(),
                'description': product.get_product_description(),
                'product_price': product.get_product_price(),
                'is_selling': product.get_product_id(),
                'seller_id': product.get_product_seller_id(),
                'buyer_id': product.get_product_id,
            })
        return productsDTO
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


