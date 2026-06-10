from PageObjectModel.Pages.cartTocheckOutpage import CartToCheckOutPage

class CartToCheckOutAction:

    def __init__(self, driver):
        self.driver = driver

    def checkout_product(
        self,
        name,
        country,
        city,
        card,
        month,
        year
    ):

        self.driver.find_element(
            *CartToCheckOutPage.CART_BUTTON
        ).click()

        self.driver.find_element(
            *CartToCheckOutPage.PLACE_ORDER_BUTTON
        ).click()

        self.driver.find_element(
            *CartToCheckOutPage.NAME_FIELD
        ).send_keys(name)

        self.driver.find_element(
            *CartToCheckOutPage.country_FIELD
        ).send_keys(country)

        self.driver.find_element(
            *CartToCheckOutPage.city_FIELD
        ).send_keys(city)

        self.driver.find_element(
            *CartToCheckOutPage.credit_card_FIELD
        ).send_keys(card)

        self.driver.find_element(
            *CartToCheckOutPage.month_FIELD
        ).send_keys(month)

        self.driver.find_element(
            *CartToCheckOutPage.year_FIELD
        ).send_keys(year)

        self.driver.find_element(
            *CartToCheckOutPage.PURCHASE_BUTTON
        ).click()