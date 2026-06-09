import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utility import excelreader, logger
from pathlib import Path

file_path = Path(__file__).parent / "Excelfile" / "Testdata.xlsx"


class TestLogin1:
    log = logger.log_generator()

    @pytest.mark.parametrize(
        "username,password",
        excelreader.get_data(str(file_path), "Sheet1")
    )
    def test_valid1(self, username, password):

        self.log.info("========== Test Started ==========")
        self.log.info(f"Testing with Username: {username}")

        driver = webdriver.Chrome()
        self.log.info("Chrome browser launched")

        driver.maximize_window()
        self.log.info("Browser maximized")

        driver.get("https://www.demoblaze.com/")
        self.log.info("Navigated to Demoblaze application")

        wait = WebDriverWait(driver, 20)

        try:
            # Open login popup
            self.log.info("Clicking Login button")
            wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

            # Enter username
            self.log.info("Entering username")
            wait.until(
                EC.visibility_of_element_located((By.ID, "loginusername"))
            ).send_keys(username)

            # Enter password
            self.log.info("Entering password")
            wait.until(
                EC.visibility_of_element_located((By.ID, "loginpassword"))
            ).send_keys(password)

            # Click login
            self.log.info("Clicking Log in button")
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))
            ).click()

            # Handle possible alert (login failure case)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                self.log.error(f"Login Alert: {alert.text}")
                alert.accept()
                raise Exception("Login failed due to alert popup")
            except TimeoutException:
                pass  # No alert → continue

            # Verify login success
            self.log.info("Waiting for Welcome message")

            actual_text = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.ID, "nameofuser"))
            ).text

            self.log.info(f"Actual text displayed: {actual_text}")

            assert "Welcome" in actual_text

            self.log.info("Login Test Passed")

        except Exception as e:
            self.log.error(f"Test Failed: {str(e)}")
            raise

        finally:
            driver.quit()
            self.log.info("Browser closed")
            self.log.info("========== Test Finished ==========\n")