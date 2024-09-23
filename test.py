from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

user_data_dir = 'C:/Users/Saedi/AppData/Local/Google/Chrome/User Data'
profile = 'Default'
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile}")

driver = webdriver.Chrome(options=chrome_options)

# Now the browser will open with the extension loaded and its saved data

time.sleep(10)
# Perform your actions here
driver.get('https://www.google.com')
time.sleep(1000)
