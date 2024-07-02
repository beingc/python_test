import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element(By.ID, "kw").send_keys("selenium")
driver.find_element(By.ID, "su").click()

time.sleep(3)
driver.quit()
