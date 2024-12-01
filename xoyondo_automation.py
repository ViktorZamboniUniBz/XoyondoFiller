import time
import random
from selenium.webdriver.common.by import By

class XoyondoAutomation:
    def __init__(self, driver):
        self.driver = driver

    def open_xoyondo(self, link):
        # Open the Xoyondo link
        self.driver.get(link)

    def fill_xoyondo_form(self, name):
        # Fill the Xoyondo form with the given name
        input_name = self.driver.find_element(By.NAME, "name")
        input_name.send_keys(name)
        self.driver.execute_script('document.querySelector("input[type=checkbox]").click()')
        self.driver.find_element(By.XPATH, "//button[span[@class='spinner-placeholder']]").click()
