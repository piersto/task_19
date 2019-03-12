from selenium.driver.support.wait import WebDriverWait
from selenium.driver.support import expected_conditions as EC
from selenium.driver.support.select import Select


class HomeHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        driver = self.app.driver

        driver.get("http://localhost/litecart/en/")
        WebDriverWait(driver, 5).until(EC.title_is('Online Store | My Store'))

    def add_item_to_the_basket(self):
        driver = self.app.driver

        driver.find_element_by_css_selector('div#box-most-popular .product').click()

        quantity_start = driver.find_element_by_css_selector('span.quantity').text
        # Find out if element present
        if len(driver.find_elements_by_css_selector("[name='options[Size]']")) > 0:
            # If element is present, select 'Small' from drop-down menu
            Select(driver.find_element_by_name("options[Size]")).select_by_visible_text("Small")
            driver.find_element_by_name('add_cart_product').click()
        else:
            # If not present Click on 'Add to cart' button
            driver.find_element_by_name('add_cart_product').click()
        wait = WebDriverWait(driver, 5)  # seconds
        wait.until(lambda d: d.find_element_by_css_selector('span.quantity').text != quantity_start)

        # Go back to Home page
        driver.find_element_by_css_selector("li a[href$='/litecart/en/']").click()
