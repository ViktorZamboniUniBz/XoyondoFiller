import random
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
        
        print("Starting the automation - Opening Whatsapp...")
        
        # Open WhatsApp Web
        whatsapp_automation.open_whatsapp(LINK_WHATSAPP)
        
        # Click the first chat
        whatsapp_automation.click_chat('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span')
        
        pattern = create_xoyondo_pattern()
        
        while True:
            print("Checking for new messages...")
            
            # Get the latest messages
            messages = whatsapp_automation.get_last_messages(
                "//*[@id='main']/div[3]/div/div[2]/div[3]",
                "//span[contains(@class, '_ao3e selectable-text copyable-text')]"
            )
            
            # Find Xoyondo links
            xoyondo_links = whatsapp_automation.find_xoyondo_links(messages, pattern)
            
            # Filter out links that have already been processed
            new_links = [link for link in xoyondo_links if not whatsapp_automation.is_link_processed(link)]
            
            if new_links:
                # Process the first new link found
                link_to_process = new_links[0]
                print(f"Processing new Xoyondo link: {link_to_process}")
                whatsapp_automation.save_link(link_to_process)
                xoyondo_automation.open_xoyondo(link_to_process)
                time.sleep(random.uniform(3, 6))
                xoyondo_automation.fill_xoyondo_form("Viktor")
                break  # Exit the loop after processing a new link
            else:
                print("No new Xoyondo links found. Retrying in a few seconds...")
                time.sleep(5)  # Wait before checking again
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Take a screenshot and close the driver
        driver_manager.take_screenshot()
        driver_manager.close_driver()

if __name__ == "__main__":
    main()
