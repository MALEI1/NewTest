#author:malei
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('c:/driver/chromedriver.exe')
driver.get('https://www.baidu.com')
driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('hello')
jquery_button = 'document.querySelectorAll("#su")[0].click();'
driver.execute_script(jquery_button)
