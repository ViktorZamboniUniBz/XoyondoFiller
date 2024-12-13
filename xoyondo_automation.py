from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class XoyondoAutomation:
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def open_xoyondo(self, link):
        self.driver.get(link)
        self.wait.until(EC.presence_of_element_located((By.NAME, "name")))

    def fill_xoyondo_form(self, name):
        # Fill the Xoyondo form with the given name
        input_name = self.driver.find_element(By.NAME, "name")
        input_name.send_keys(name)
        self.driver.execute_script('document.querySelector("input[type=checkbox]").click()')
        self.driver.find_element(By.XPATH, "//button[span[@class='spinner-placeholder']]").click()
