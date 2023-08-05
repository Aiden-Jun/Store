from User import Seller, Buyer
from Card import Card
from Manager import Manager
from Product import Product
from oop.Auth import Auth


class Store:
    def __init__(self):
        self.manager = Manager()

    def start(self):
        # 가입, 로그인
        auth = Auth()
        auth.show_prompt()

        # 로그인 시도
        # 이메일, 비밀번호 입력 받기
        # 진짜 이메일, 비밀번호가 일치하는 유저가 존재하는지 확인(데이터베이스 사용)
        # 유저가 있다 => 메인 화면 보여주기
        # 유저가 없다 => 다시 가입 로그인 화면으로 돌아가기


        # Seller
        seller_1 = Seller('yellowbird@gmail.com', 'yellow', '노랑이', '010-2129-1123', self.manager)
        seller_1_card = Card('551233', 2000, '254')
        seller_1.set_card(seller_1_card)

        # Buyer
        buyer_1 = Buyer('redbird@gmail.com', 'red', '빨강이', self.manager)
        buyer_1_card = Card('123483', 1000, '712')
        buyer_1.set_card(buyer_1_card)

        # Changing Balance
        seller_1.change_balance(100)
        buyer_1.change_balance(100)

        # Products
        laptop = Product('Macbook Pro', 'Ultra Fast Macbook Pro, buy today', 40, seller_1)

        # Adding Product
        seller_1.add_product(laptop)

        # Printing all seller and their products
        print(self.manager.get_all_seller_and_products())

        # Adding to cart and buying a product
        buyer_1.add_to_cart(seller_1.get_user_id(), 0)
        print(buyer_1.get_cart())
        buyer_1.buy_cart()

        # Printing all seller and their products
        print(self.manager.get_all_seller_and_products())

        # Printing buyer's history
        print(buyer_1.get_history())

        # Printing balances
        print(seller_1.get_balance())
        print(buyer_1.get_balance())


# This runs when Main.py is not imported
if __name__ == '__main__':
    store = Store()
    store.start()