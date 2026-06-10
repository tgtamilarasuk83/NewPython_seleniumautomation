from selenium.webdriver.common.by import By
class CartToCheckOutPage:
    
    CART_BUTTON = (By.XPATH, "//a[normalize-space()='Cart']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Place Order']")
    NAME_FIELD = (By.XPATH, "//*[@id='name']")
    country_FIELD = (By.XPATH, "//*[@id='country']")
    city_FIELD = (By.XPATH, "//*[@id='city']")
    credit_card_FIELD = (By.XPATH, "//*[@id='card']")
    month_FIELD = (By.XPATH, "//*[@id='month']")
    year_FIELD = (By.XPATH, "//*[@id='year']")
    PURCHASE_BUTTON = (By.XPATH, "//button[normalize-space()='Purchase']")