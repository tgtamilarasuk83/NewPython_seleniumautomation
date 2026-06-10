from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.Pages.Loginpage import LoginPage
import time

class LoginAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def login(self, username, password):
        self.wait.until(
            EC.element_to_be_clickable(LoginPage.LOGIN_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(LoginPage.USERNAME)
        ).send_keys(username)

        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(LoginPage.SUBMIT_BUTTON)
        ).click()
        time.sleep(10)