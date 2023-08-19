from Database import Database
from oop.Infrastructure.Repository import Repository


class AuthService(object):
    def __init__(self):
        self.choice = None
        print("뭐지...?")
        self.__db = Database() # 없어져야 함
        self.__repository = Repository()

    def find_user(self, email, password):
        user = self.__repository.get_user(email)
        if user != None:
            if user[1] == password:
                return user
        return None

    def add_user(self, email, password, name, type):
        self.__db.add_user_row(email, password, name, type)

    def does_this_email_exist(self, email):
        return self.__db.check_email_existence(email)