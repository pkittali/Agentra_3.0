from pages.base_page import BasePage

class LoginPage(BasePage):
    username = ('id', 'username')
    password = ('id', 'password')
    login_button = ('xpath', "//button[@type='submit']")

    def login(self, user, pwd):
        self.enter_text(*self.username, text=user)
        self.enter_text(*self.password, text=pwd)
        self.click(*self.login_button)
