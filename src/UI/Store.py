from src.UI.AuthScreen import AuthScreen
from src.UI.HomeScreen import HomeScreen


class Store:
    def __init__(self):
        self.auth_screen = AuthScreen()
        self.home_screen = HomeScreen()
        self.me = None

    def start(self):
        choice = self.auth_screen.show_option_prompt()
        if choice == 'login':
            me = self.auth_screen.sign_in()
            if me is None:
                print('No accounts found, try again')
                self.auth_screen.show_option_prompt()
            else:
                self.me = me
                self.home_screen.home(me)
        else:
            result = self.auth_screen.sign_up()
            if result is False:
                self.auth_screen.show_option_prompt()
            else:
                self.auth_screen.sign_in()


# This runs when OOP.py is not imported
if __name__ == '__main__':
    pass
