from src.Domain.User.User import User
from src.Repository.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    def create_user(self, email, password, name, user_type):
        self._db.append("users.csv", [email, password, name, user_type, 0])

    def find_user_by_email(self, email):
        user_rows = self._db.read("users.csv")
        for user_row in user_rows:
            if user_row[1] == email:
                return self.convert_user_from_row_to_object(user_row)
        return None

    def find_user_by_id(self, user_id):
        user_id = str(user_id)
        user_rows = self._db.read("users.csv")
        for user_row in user_rows:
            if user_row[0] == user_id:
                return self.convert_user_from_row_to_object(user_row)
        return None

    def find_user_by_email_and_password(self, email, password):
        user_rows = self._db.read("users.csv")
        for user_row in user_rows:
            if user_row[1] == email:
                if user_row[2] == password:
                    print('Found one')
                    return self.convert_user_from_row_to_object(user_row)
        print('Ooga thee is not any - User repo')
        return None

    def convert_user_from_row_to_object(self, user_row):
        return User(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4], user_row[5])


if __name__ == "__main__":
    pass
