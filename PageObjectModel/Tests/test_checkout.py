from PageObjectModel.action.Loginaction import LoginAction
from PageObjectModel.action.AddTocartcation import AddToCartAction
from PageObjectModel.action.CartToCheckOutAction import CartToCheckOutAction


def test_complete_purchase_flow(setup):

    driver = setup
    driver.get("https://www.demoblaze.com")

    # Login
    login = LoginAction(driver)
    login.login("arasu", "arasu")

    # Add Product To Cart
    add_to_cart = AddToCartAction(driver)
    add_to_cart.add_to_cart()

    # Checkout
    checkout = CartToCheckOutAction(driver)
    checkout.checkout_product(
        "Tamil",
        "India",
        "Chennai",
        "1234567890123456",
        "06",
        "2026"
    )