# utilities/driver_manager.py
from selenium import webdriver

class DriverManager:
    @staticmethod
    def get_chrome_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--headless=new")  # Descomentar para headless
        return webdriver.Chrome(options=options)