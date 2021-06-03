from selenium import webdriver

PATH = './chromedriver';
driver = webdriver.Chrome(PATH)
print(webdriver.support)
driver.get('https://qquant.online')
driver.quit()
