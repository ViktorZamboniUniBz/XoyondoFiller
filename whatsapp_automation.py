# whatsapp_automation.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsappAutomation:
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
    
    def open_whatsapp(self, link):
        self.driver.get(link)

    def click_chat(self, xpath):
        chat_button = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        chat_button.click()

    def get_last_messages(self, chat_xpath, message_xpath, num_messages=5):
        chat = self.driver.find_element(By.XPATH, chat_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", chat)
        time.sleep(2)
        
        messages = chat.find_elements(By.XPATH, message_xpath)[-num_messages:]
        return messages

    def find_xoyondo_links(self, messages, pattern):
        links = []
        for message in messages:
            message_text = message.text
            anchors = message.find_elements(By.TAG_NAME, "a")
            xoyondo_links = [link.get_attribute('href') for link in anchors if "xoyondo.com" in link.get_attribute('href')]
            if xoyondo_links:
                links.extend(xoyondo_links)
            elif pattern.search(message_text):
                links.append(pattern.search(message_text).group())
        return links
