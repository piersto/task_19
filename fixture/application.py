from selenium import driver
from fixture.home import HomeHelper
from fixture.basket import BasketHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.driver = driver.Chrome()
        elif browser == 'firefox':
            self.driver = driver.Firefox()
        elif browser == 'ie':
            self.driver = driver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.driver.maximize_window()
        self.home = HomeHelper(self)
        self.basket = BasketHelper(self)

    def go_back_to_home_page(self):
        driver = self.driver
        driver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()

    def destroy(self):
        self.driver.quit()

