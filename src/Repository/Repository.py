from Domain.User.User import User
from Infrastructure.Database import Database


class Repository(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__db = Database()

    def find_user_by_email(self, email):
        user_rows = self.__db.read("users.csv")
        for user_row in user_rows:
            if user_row[0] == email:
                return user_row
        return None

    def find_user_by_email_and_password(self, email, password):
        user_rows = self.__db.read("users.csv")
        for user_row in user_rows:
            if user_row[0] == email:
                return self.convert_user_from_row_to_object(user_row)
        return None

    def add_user(self, email, password, name, user_type):
        self.__db.write("users.csv", [email, password, name, user_type])

    def convert_user_from_row_to_object(self, user_row):
        return User(user_row[0], user_row[1], user_row[2], 0)
