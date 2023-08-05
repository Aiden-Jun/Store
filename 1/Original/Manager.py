

class Manager(object):
    def __init__(self):
        self.all_products = {}

    # {userId:[], }

    def register_seller(self, seller_id):
        self.all_products[seller_id] = []
        
    def add_product(self, seller_id, product):
        self.all_products[seller_id].append(product)

    def view_product(self, product_index, seller_id):
        return self.all_products[seller_id][product_index]