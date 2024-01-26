import undetected_chromedriver as quiet_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
now = datetime.now()

options = quiet_webdriver.ChromeOptions()
profile = "C:\\Users\\quade\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")
quiet_driver = quiet_webdriver.Chrome(options=options,use_subprocess=True)
quiet_driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
quiet_driver.implicitly_wait(10)

actions = ActionChains(quiet_driver)
actions.send_keys("casey.gibson@selu.edu" + Keys.TAB + Keys.TAB + "From Snakey Boy" + Keys.TAB + 
"Hello This was sent by snake man" + Keys.TAB + Keys.ENTER)
actions.perform()




time.sleep(30)

