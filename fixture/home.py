from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        self.app.get("http://localhost/litecart/en/")
        WebDriverWait(self, 10).until(EC.title_is('Online Store | My Store'))

