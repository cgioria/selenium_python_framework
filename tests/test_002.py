from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pytest

@pytest.fixture(scope="class")
def driver_init(request):
    # Configuración inicial
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    request.cls.driver = driver
    yield
    # Limpieza
    driver.quit()

@pytest.mark.usefixtures("driver_init")
class TestLogin:
    # Test 1: Login exitoso
    def test_successful_login(self):
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "secure" in self.driver.current_url

    # Test 2: Login fallido
    def test_failed_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.find_element(By.ID, "username").send_keys("wrong")
        self.driver.find_element(By.ID, "password").send_keys("wrong")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "Your username is invalid!" in self.driver.find_element(By.ID, "flash").text

    # Test 3: Campos vacíos
    def test_empty_fields(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        assert "Username is required" in self.driver.find_element(By.ID, "flash").text