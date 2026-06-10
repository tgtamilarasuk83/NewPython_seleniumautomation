import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.Pages.AddtocartPage import AddToCartPage


class AddToCartAction:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_to_cart(self):
       
       
        self.wait.until(
            EC.element_to_be_clickable(AddToCartPage.LAPTOP_BUTTON)
        ).click()

        # Click MacBook Pro
        self.wait.until(
            EC.element_to_be_clickable(AddToCartPage.MACBOOK_BUTTON)
        ).click()

        # Click Add to cart
        self.wait.until(
            EC.element_to_be_clickable(AddToCartPage.CART_BUTTON)
        ).click()

       
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()