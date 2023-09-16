class User(object):
    def __init__(self, user_id, email, password, name, money, user_type):  # Manager class object is passed in
        self._user_id = int(user_id)
        self._email = email
        self._password = password
        self._name = name
        self._money = int(money)
        self._user_type = user_type

    def get_user_id(self):
        return self._user_id

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_name(self):
        return self._name

    def get_money(self):
        return self._money

    def get_user_type(self):
        return self._user_type

    def change_name(self, new_name):
        self._name = new_name

    def income(self, amount):
        self._money += amount

    def expense(self, amount):
        self._money -= amount

    def convert_domain_to_dto(self):
        return {
            "user_id": self.get_user_id(),
            "email": self.get_email(),
            "name": self.get_name(),
            "money": self.get_money(),
            "user_type": self.get_user_type(),
        }


if __name__ == "__main__":
    pass
