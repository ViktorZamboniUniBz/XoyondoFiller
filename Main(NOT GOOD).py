import time
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
#import pyautogui
import random


linkWhatsapp = 'https://web.whatsapp.com/'
linkXoyondo = None
options = uc.ChromeOptions()
options.add_argument("--profile-directory=Profile 2")
options.add_argument("--user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 5)
trovato = False
xoyondo_pattern = re.compile(r'https?://(?:www\.)?xoyondo\.com/op/\S+')

try:
    driver.get(linkWhatsapp)
    #time.sleep(10)
    #driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[18]/div/div/div/div[2]/div[1]/div[1]/span').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span'))).click()
    chat = driver.find_element(By.XPATH, "//*[@id="'"main"'"]/div[3]/div/div[2]/div[3]")
    driver.execute_script("arguments[0].scrollIntoView(false);", chat)
    time.sleep(2)
    while trovato == False:
        print(trovato)
    # Trova i messaggi e seleziona gli ultimi 5
        messages = chat.find_elements(By.XPATH, "//span[contains(@class, '_ao3e selectable-text copyable-text')]")[-5:]


        for i, message in enumerate(messages, 1):
            message_text = message.text
            links = message.find_elements(By.TAG_NAME, "a")
            xoyondo_links = [link.get_attribute('href') for link in links if "xoyondo.com" in link.get_attribute('href')]
        if xoyondo_links:
            print(f"Messaggio {i} contiene un link Xoyondo sas:")
            linkXoyondo = xoyondo_links[-1]
            trovato = True
        elif xoyondo_pattern.search(message_text):  # Verifica link Xoyondo nel testo
            linkXoyondo = xoyondo_pattern.search(message_text).group()
            trovato = True
        time.sleep(3)
except Exception as e:
    print(e)

try:
    linkXoyondo = "https://xoyondo.com/op/c69xidpfs6ryr78"
    driver.get(linkXoyondo)
    time.sleep(random.uniform(2, 5))
    # driver.execute_script('document.querySelector("body > div.cmp-root-container").shadowRoot.querySelector("#consentDialog > div.cmp_ui.cmp_ext_text.cmp_state-stacks > div.cmp_navi > div > div.cmp_mainButtons > div > div.cmp_primaryButtonLine > div > div > div").click()')
    # driver.execute_script('document.querySelector("#cb-1185459").click()')
    #driver.execute_script('document.querySelector("input[type=\'text\']").value = "Adnan"')
    input_name = driver.find_element(By.NAME, "name")
    input_name.send_keys("Viktor")
    #input_box.click()
    #input_box.send_keys("Adnan")
    driver.execute_script('document.querySelector("input[type=checkbox]").click()')
    driver.find_element(By.XPATH, "//button[span[@class='spinner-placeholder']]").click()
#     # time.sleep(3)
#     # for i in range(1, 5):
#     #     pyautogui.moveTo(random.randint(0, 1900), random.randint(0, 1000), duration=5)
#     # pyautogui.moveTo(67, 432, duration=4)
#     # pyautogui.click()
    
    
finally:
     time.sleep(3)
     driver.quit()


