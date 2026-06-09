from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datadrivenconcept.ConfigReader import (
    get_application_url,
    get_browser,
    get_username,
    get_password,
    get_invalidusername,
    get_invalidpassword
)


def get_driver():
    browser = get_browser().lower()

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Invalid browser in config.ini")

    driver.maximize_window()
    return driver



def test_login():

    driver = get_driver()
    driver.get(get_application_url())

    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    username_box = wait.until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    username_box.clear()
    username_box.send_keys(get_username())

    password_box = wait.until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    password_box.clear()
    password_box.send_keys(get_password())

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))
    ).click()

    actual_text = wait.until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    ).text

    expected_text = "Welcome arasu"

    assert actual_text == expected_text

    driver.quit()



def test_invalidlogin():

    driver = get_driver()
    driver.get(get_application_url())

    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    username_box = wait.until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    username_box.clear()
    username_box.send_keys(get_invalidusername())

    password_box = wait.until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    password_box.clear()
    password_box.send_keys(get_invalidpassword())

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))
    ).click()

    # ---------------------------
    # Handle alert safely
    # ---------------------------
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()

    print("Alert message:", alert_text)

    # Optional assertion (recommended)
    assert alert_text is not None

    driver.quit()