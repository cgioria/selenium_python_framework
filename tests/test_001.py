from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


# Configuration - Set these values according to your system
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"  # Update this path
CHROME_BINARY_PATH = "/usr/bin/google-chrome"  # Optional: Only if Chrome is not in default location

class TestSeleniumUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--headless=new")  # Opcional
        service = Service(executable_path=CHROMEDRIVER_PATH)
        cls.driver = webdriver.Chrome(service=service, options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_simple_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_button.click()
        # Validar que el div con id="flash" y clase="flash success" existe y contiene el mensaje correcto
        flash_div = self.driver.find_element(By.ID, "flash")
        self.assertIn("flash success", flash_div.get_attribute("class"))
        self.assertIn("You logged into a secure area!", flash_div.text)



