from src.Domain.User.Buyer import Buyer
from src.Domain.User.Seller import Seller
from src.Domain.User.User import User
from src.Infrastructure.Database import Database


class UserRepository(object):
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
            if user_row[1] == email:
                if user_row[2] == password:
                    print('Found one')
                    return self.convert_user_from_row_to_object(user_row)
        print('Ooga thee is not any - User repo')
        return None

    def add_user(self, email, password, name, user_type):
        self.__db.write("users.csv", [email, password, name, user_type, 0])

    def update_user_name(self, user_id, new_name):
        user_rows = self.__db.read("users.csv")
        for user_row in user_rows:
            if user_row[0] == user_id:
                user_row[3] = new_name
                self.__db.write('users.csv', user_rows)
                return

    def convert_user_from_row_to_object(self, user_row):
        if user_row[3] == 'seller':
            return Seller(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5], self)
        else:
            return Buyer(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5], self)


if __name__ == "__main__":
    pass
