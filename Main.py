import time
from driver_manager import DriverManager
from whatsapp_automation import WhatsappAutomation
from xoyondo_automation import XoyondoAutomation
from utils import create_xoyondo_pattern
from config import LINK_WHATSAPP, PROFILE_DIRECTORY, USER_DATA_DIR

def main():
    # Setup driver
    driver_manager = DriverManager(PROFILE_DIRECTORY, USER_DATA_DIR)
    driver = driver_manager.setup_driver()

    try:
        # Setup Whatsapp and Xoyondo automation
        whatsapp_automation = WhatsappAutomation(driver)
        xoyondo_automation = XoyondoAutomation(driver)
        
        # Open WhatsApp Web
        whatsapp_automation.open_whatsapp(LINK_WHATSAPP)
        
        # Click the first chat
        whatsapp_automation.click_chat('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span')
        
        #find the last messages and check if there is a Xoyondo link
        messages = whatsapp_automation.get_last_messages("//*[@id='main']/div[3]/div/div[2]/div[3]", "//span[contains(@class, '_ao3e selectable-text copyable-text')]")
        pattern = create_xoyondo_pattern()
        xoyondo_links = whatsapp_automation.find_xoyondo_links(messages, pattern)
        
        #if found, open the last link and fill the form
        if xoyondo_links:
            print(f"Found Xoyondo link(s): {xoyondo_links}")
            xoyondo_automation.open_xoyondo(xoyondo_links[-1])
            xoyondo_automation.fill_xoyondo_form("Viktor")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Take a screenshot and close the driver
        driver_manager.take_screenshot()
        time.sleep(3)
        driver_manager.close_driver()

if __name__ == "__main__":
    main()
