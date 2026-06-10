import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_home_page(driver):
    assert "tutorialsninja.com" in driver.current_url.lower()


def test_search_product(driver):
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.input-lg"))
    )

    search.send_keys("HP")
    search.send_keys(Keys.ENTER)

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1"))
    )

    assert "Search - HP" in result.text


def test_valid_product(driver):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )

    search_box.send_keys("iPhone")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    iphone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "iPhone"))
    )

    assert iphone.is_displayed()


def test_invalid_product(driver):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )

    search_box.send_keys("pulsar")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    actual_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'There is no product')]")
        )
    ).text

    expected_text = "There is no product that matches the search criteria."

    assert expected_text in actual_text


def test_no_product_found(driver):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )

    search_box.send_keys("nx100")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    actual_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'There is no product')]")
        )
    ).text

    expected_text = "There is no product that matches the search criteria."

    assert expected_text in actual_text