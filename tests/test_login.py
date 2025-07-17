# tests/test_login.py
import unittest
from pages.login_page import LoginPage
from utilities.driver_manager import DriverManager

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverManager.get_chrome_driver()
        cls.login_page = LoginPage(cls.driver)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.login_page.navigate_to_login()
    
    def test_successful_login(self):
        self.login_page.login("tomsmith", "SuperSecretPassword!")
        self.assertTrue(self.login_page.is_login_successful())
        self.assertIn("You logged into a secure area!", self.login_page.get_flash_message())
    
    def test_failed_login(self):
        self.login_page.login("wrong_user", "wrong_password")
        self.assertIn("Your username is invalid!", self.login_page.get_flash_message())
    
    def test_empty_fields(self):
        self.login_page.login("", "")
        self.assertIn("Username is required", self.login_page.get_flash_message())

if __name__ == "__main__":
    unittest.main()