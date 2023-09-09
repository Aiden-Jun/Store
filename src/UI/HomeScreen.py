from src.Service.Service import Service


class HomeScreen(object):
    def __init__(self):
        self.service = Service()
        self.me = None

    def home(self, me):
        print('This is main screen (Not done YET)')
        self.me = me
        if me['user_type'] == 'buyer':
            self.buyer_main_ui()

    def buyer_main_ui(self):
        print(f'buyer, 이메일: {self.me["email"]}, 잔액: {self.me["money"]}')
        bought_products = self.service.get_product_service().get_buy_products(self.me['user_id'])

        print()
        print("==============================================================")
        for bought_product in bought_products:
            print(f"구매한 상품: {bought_product['product_id']},{bought_product['product_name']}")
        selling_products = self.service.get_product_service().get_selling_products()
        print("==============================================================")
        for selling_product in selling_products:
            print(f"판매중인 상품: {selling_product['product_id']},{selling_product['product_name']}")
        print("==============================================================")
        print()

        product_id = input("구매할 상품의 아이디를 입력하세요: ")
        if product_id == 'quit':
            quit()

