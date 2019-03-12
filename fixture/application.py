from selenium import webdriver
from fixture.home import HomeHelper
from fixture.basket import BasketHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.webdriver = webdriver.Chrome()
        elif browser == 'firefox':
            self.webdriver = webdriver.Firefox()
        elif browser == 'ie':
            self.webdriver = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.webdriver.implicitly_wait(5)
        self.base_url = base_url
        self.webdriver.maximize_window()
        self.home = HomeHelper(self)
        self.basket = BasketHelper(self)

    def destroy(self):
        self.webdriver.quit()

