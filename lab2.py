from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Define Browser Options
chrome_options = Options()
chrome_options.add_argument("--headless") # Hides the browser window
# Reference the local Chromedriver instance
PATH = './chromedriver';
driver = webdriver.Chrome(executable_path=PATH)
driver.get('https://techwithtim.net')

link  = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver,3).until(
        EC.presence_of_element_located((By.LINK_TEXT,'Beginner Python Tutorials'))
    )
    element.click()
    # driver.back()
    # driver.forward()
finally:
    driver.quit()