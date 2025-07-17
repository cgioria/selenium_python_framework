# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def navigate_to_login(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
    
    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_flash_message(self):
        return self.is_element_visible(self.FLASH_MESSAGE).text
    
    def is_login_successful(self):
        return "secure" in self.driver.current_url