from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 

#define Browser optoin 
ch_op = Options() 
ch_op.add_argument("--headless")
PATH = './chromedriver'; 
driver  = webdriver.Chrome(executable_path=PATH) 
driver.get('https://google.com')

body = driver.find_element_by_tag_name('input')
print(body)
print(body.text)