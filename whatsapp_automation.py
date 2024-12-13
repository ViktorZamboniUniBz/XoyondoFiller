import json
import os
import time
from config import HISTORY_FILE_PATH
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsappAutomation:
    def __init__(self, driver, wait_time=5, history_file=HISTORY_FILE_PATH):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
        self.history_file = history_file
        self._initialize_history_file()

    def _initialize_history_file(self):
        """Crea il file JSON se non esiste."""
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w") as file:
                json.dump([], file)
                
    def save_link(self, link):
        """Salva un link nel file JSON e mantiene solo gli ultimi 10."""
        with open(self.history_file, "r") as file:
            history = json.load(file)
        
        if link not in history:
            history.append(link)
            if len(history) > 10:
                history = history[-10:]
            with open(self.history_file, "w") as file:
                json.dump(history, file)

    def is_link_processed(self, link):
        """Verifica se un link è già stato processato."""
        with open(self.history_file, "r") as file:
            history = json.load(file)
        return link in history
    
    def open_whatsapp(self, link):
        self.driver.get(link)
        self.wait.until(EC.presence_of_element_located((By.ID, "pane-side")))

    def click_chat(self, xpath):
        # Find the chat button and click it
        chat_button = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        chat_button.click()

    def get_last_messages(self, chat_xpath, message_xpath, num_messages=3):
        # Find the chat and scroll to it
        chat = self.driver.find_element(By.XPATH, chat_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", chat)
        time.sleep(2)
        
        # Find the last messages
        messages = chat.find_elements(By.XPATH, message_xpath)[-num_messages:]
        return messages

    def find_xoyondo_links(self, messages, pattern):
        # Find Xoyondo links in the messages
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
