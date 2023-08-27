from Store.UI.AuthScreen import AuthScreen
from Store.UI.HomeScreen import HomeScreen


class Store:
    def __init__(self):
        self.home_screen = HomeScreen()
        self.auth_screen = AuthScreen()

    def start(self):
        choice = self.auth_screen.show_option_prompt()
        if choice == 'login':
            me = self.auth_screen.sign_in()
            if me is None:
                self.auth_screen.show_option_prompt()
            else:
                self.home_screen.home()
        else:
            result = self.auth_screen.sign_up()
            if result is False:
                self.auth_screen.show_option_prompt()
            else:
                self.auth_screen.sign_in()


# This runs when Store.py is not imported
if __name__ == '__main__':
    pass
