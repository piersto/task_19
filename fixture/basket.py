from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasketHelper:

    def __init__(self, app):
        self.app = app

    def remove_items(self):
        webdriver = self.app.webdriver

        self.app.hopen_home_page()

        buttons = webdriver.find_elements_by_css_selector("[name='remove_cart_item']")

        for i in range(len(buttons)):
            len_old_list = len(webdriver.find_elements_by_css_selector("tr td.item"))

            wait = WebDriverWait(webdriver, 5)  # seconds
            button = wait.until(EC.visibility_of_element_located((By.NAME, "remove_cart_item")))
            button.click()

            wait.until(lambda driver: len(driver.find_elements_by_css_selector("tr td.item")) < len_old_list)

            webdriver.find_elements_by_css_selector("[name='remove_cart_item']")




