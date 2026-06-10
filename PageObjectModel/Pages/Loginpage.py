from selenium.webdriver.common.by import By

class LoginPage:

    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[@onclick='logIn()']")