from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class HomeHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        webdriver = self.app.webdriver

        webdriver.get("http://localhost/litecart/en/")
        WebDriverWait(webdriver, 5).until(EC.title_is('Online Store | My Store'))

    def add_item_to_the_basket(self):
        webdriver = self.app.webdriver

        webdriver.find_element_by_css_selector('div#box-most-popular .product').click()

        quantity_start = webdriver.find_element_by_css_selector('span.quantity').text
        # Find out if element present
        if len(webdriver.find_elements_by_css_selector("[name='options[Size]']")) > 0:
            # If element is present, select 'Small' from drop-down menu
            Select(webdriver.find_element_by_name("options[Size]")).select_by_visible_text("Small")
            webdriver.find_element_by_name('add_cart_product').click()
        else:
            # If not present Click on 'Add to cart' button
            webdriver.find_element_by_name('add_cart_product').click()
        wait = WebDriverWait(webdriver, 5)  # seconds
        wait.until(lambda d: d.find_element_by_css_selector('span.quantity').text != quantity_start)

        # Go back to Home page
        webdriver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()
