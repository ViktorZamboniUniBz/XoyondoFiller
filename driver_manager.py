import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

class DriverManager:
    def __init__(self, profile_directory: str, user_data_dir: str):
        # Set the profile directory and user data directory
        self.profile_directory = profile_directory
        self.user_data_dir = user_data_dir
        self.driver = None

    def setup_driver(self):
        # Setup the driver with the profile directory and user data directory
        options = uc.ChromeOptions()
        options.add_argument(f"--profile-directory={self.profile_directory}")
        options.add_argument(f"--user-data-dir={self.user_data_dir}")
        
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            
    def take_screenshot(self, save_path='C:\\Users\\User\\Documents\\diagrammaEr\\XoyondoFiller\\screenshots', screenshot_name='screenshot.png'):
        # Create a dir if it doesn't exist
        os.makedirs(save_path, exist_ok=True)
        
        # Define the path of the screenshot
        screenshot_path = os.path.join(save_path, screenshot_name)
        
        # save the screenshot
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot salvato in: {screenshot_path}")
