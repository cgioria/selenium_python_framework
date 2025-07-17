# test_login.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://the-internet.herokuapp.com/login")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Test 1: Login exitoso
    def test_successful_login(self):
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertIn("secure", self.driver.current_url)

    # Test 2: Login fallido
    def test_failed_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")  # Recargar página
        self.driver.find_element(By.ID, "username").send_keys("sasasasddd")
        self.driver.find_element(By.ID, "password").send_keys("ghhgjjjjk")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertIn("Your username is invalid!", self.driver.find_element(By.ID, "flash").text)

    # Test 3: Campos vacíos
    def test_empty_fields(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertIn("Username is required", self.driver.find_element(By.ID, "flash").text)

