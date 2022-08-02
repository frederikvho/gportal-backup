"""
Useful Links:
https://selenium-python.readthedocs.io/waits.html
"""

import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME,
)

# Wait up to 10 seconds for any element we're looking for to load
driver.implicitly_wait(10)

driver.get(os.environ["GPORTAL_BACKUP_URL"])

# Navigate Authentication
#driver.find_element_by_id("username").send_keys(os.environ["GPORTAL_EMAIL"])
#driver.find_element_by_id("password").send_keys(os.environ["GPORTAL_PASSWORD"])
#driver.find_element_by_id("kc-login").click()

# Navigate Authentication
driver.find_element("name", "username").send_keys(os.environ["GPORTAL_EMAIL"])
driver.find_element("name", "password").send_keys(os.environ["GPORTAL_PASSWORD"])
driver.find_element("name", "login").click()


# Deubgging: print the contents
# print(driver.page_source)

# Create Backup
driver.find_element("id", "make_backup").click()
driver.find_element(By.CSS_SELECTOR, "body > div.dialog.dialog--size-default > div > div > div > div > button:nth-child(2)").click()
