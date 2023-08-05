from User import Buyer, Seller
from Product import Product
from Card import Card
from Manager import Manager

class Coupang(object):
    def __init__(self):
        self.manager = Manager()

    def start(self):
        seller1 = Seller("노랑이", "xxx@gmail.com", 1234, "010-0000-0000", 1000, self.manager)
        seller1_card = Card("987654", 100, seller1)
        seller1.set_card(seller1_card)


        buyer1 = Buyer("빨강이", "yyy@gmail.com", 1234, self.manager)
        buyer1_card = Card("123456", 1000, buyer1)
        buyer1.set_card(buyer1_card)

        print(seller1.get_name())

        for i in range(100):
            product1 = Product("노트북", "겁나 빠른 노트북", i, seller1)
            seller1.add_product(product1)

        buyer1.add_to_cart(0, seller1.get_id)




        


if __name__ == '__main__':
    coupang = Coupang()
    coupang.start()