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

    def buy_product_using_id(self, product_id, buyer_id):
        '''
        1. Authenticate Buyer ID -
        2. Get Product Status -
        3. Get Product price 
        5. Get Buyer Balance Status
        4. Find seller
        5. Add amount to seller's card
        6. Decrease balance on buyer's card
        7. Change Product is Selling Status
        8. Add buyer to product csv
        9. Add product to buyer's history
        10. Give product
        '''

        buyer_obj = self.__repository.get_user_repository().find_user_by_id(buyer_id)
        # Authenticate Buyer ID
        if buyer_obj is None:
            print('Auth Fail')
            return False

        # Get product status
        product_obj = self.__repository.get_product_repository().find_product_using_id(product_id)
        if product_obj is None:
            print('Status Fail')
            return False
        
        if product_obj.is_product_selling() is False:
            print('Not Selling Fail')
            return False

        # Buyer Balance Check
        if buyer_obj.get_balance() < product_obj.get_product_price():
            print('Balance Fail')
            return False
        
        # Buying Process
        # Pay Seller
        seller_obj = self.__repository.get_user_repository().find_user_by_id(product_obj.get_product_seller_id())
        self.__repository.get_user_repository().update_user_money(product_obj.get_product_seller_id(), seller_obj.get_balance() + product_obj.get_product_price())

        # Decrease buyer money
        self.__repository.get_user_repository().update_user_money(buyer_id, buyer_obj.get_balance() - product_obj.get_product_price())

        # Product Status change
        self.__repository.get_product_repository().update_product_selling_status(product_id, buyer_id, '0')

        return True


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
