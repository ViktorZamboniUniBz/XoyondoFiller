# driver_manager.py
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverManager:
    def __init__(self, profile_directory: str, user_data_dir: str):
        self.profile_directory = profile_directory
        self.user_data_dir = user_data_dir
        self.driver = None

    def setup_driver(self):
        options = uc.ChromeOptions()
        options.add_argument(f"--profile-directory={self.profile_directory}")
        options.add_argument(f"--user-data-dir={self.user_data_dir}")
        
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
