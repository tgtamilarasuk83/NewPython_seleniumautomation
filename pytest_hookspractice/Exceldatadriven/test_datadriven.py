import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utility import excelreader, logger
from pathlib import Path

file_path = Path(__file__).parent / "Excelfile" / "Testdata.xlsx"


class TestLogin1:
    logger = logger.log_generator()

    @pytest.mark.parametrize(
        "username,password",
        excelreader.get_data(str(file_path), "Sheet1")
    )
    def test_valid1(self, username, password):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.demoblaze.com/")

        wait = WebDriverWait(driver, 30)

        try:
            wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

            wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
            wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()

            actual_text = wait.until(
                EC.visibility_of_element_located((By.ID, "nameofuser"))
            ).text

            assert "Welcome" in actual_text

        finally:
            driver.quit()