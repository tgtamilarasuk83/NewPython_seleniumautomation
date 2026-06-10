from PageObjectModel.action.Loginaction import LoginAction

def test_login(setup):
    driver = setup

    driver.get("https://www.demoblaze.com")

    login_action = LoginAction(driver)
    login_action.login("arasu", "arasu")