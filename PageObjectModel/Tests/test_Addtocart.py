from PageObjectModel.action.Loginaction import LoginAction
from PageObjectModel.action.AddTocartcation import AddToCartAction


def test_add_to_cart(setup):

    driver = setup
    driver.get("https://www.demoblaze.com")

    login_action = LoginAction(driver)
    login_action.login("arasu", "arasu")

    cart_action = AddToCartAction(driver)
    cart_action.add_to_cart()