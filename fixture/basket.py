from selenium.driver.support.wait import WebDriverWait
from selenium.driver.support import expected_conditions as EC
from selenium.driver.common.by import By


class BasketHelper:

    def __init__(self, app):
        self.app = app

    def remove_items(self):
        driver = self.app.driver

        self.app.home.open_home_page()

        driver.find_element_by_css_selector("a[href$='/en/checkout']").click()

        buttons = driver.find_elements_by_css_selector("[name='remove_cart_item']")
        for i in range(len(buttons)):
            len_old_list = len(driver.find_elements_by_css_selector("tr td.item"))

            wait = WebDriverWait(driver, 5)  # seconds
            button = wait.until(EC.visibility_of_element_located((By.NAME, "remove_cart_item")))
            button.click()

            wait.until(lambda driver: len(driver.find_elements_by_css_selector("tr td.item")) < len_old_list)

            driver.find_elements_by_css_selector("[name='remove_cart_item']")




