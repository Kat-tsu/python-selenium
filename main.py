from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = './chromedriver';
driver = webdriver.Chrome(PATH)
driver.get('https://techwithtim.net/')
print(driver.title)

# search = driver.find_element_by_name("s")
s = driver.find_element_by_name('s')
s.send_keys("testing")
s.send_keys(Keys.RETURN)
# print(driver.page_source)

try: 
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"main"))
    )
    articles = element.find_element_by_tag_name("article") 
    print(articles.text)
    for article in  list(articles.text):
        header = articles.find_element_by_class_name("entry-title")
        print(header.text)
finally:
    driver.quit()
# main = driver.find_element_by_id("main");



