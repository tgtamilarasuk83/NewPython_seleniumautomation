from selenium.webdriver.common.by import By


class AddToCartPage:

    LAPTOP_BUTTON = (By.LINK_TEXT, "Laptops")
    MACBOOK_BUTTON = (By.XPATH, "//a[normalize-space()='MacBook Pro']")
    CART_BUTTON = (By.XPATH, "//a[contains(@onclick,'addToCart')]")