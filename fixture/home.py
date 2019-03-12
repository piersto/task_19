from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        webdriver = self.app.webdriver
        webdriver.get("http://localhost/litecart/en/")
        WebDriverWait(webdriver, 10).until(EC.title_is('Online Store | My Store'))

