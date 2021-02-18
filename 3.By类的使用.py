#author:malei
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:/driver/chromedriver.exe")
# driver.find_element_by_id('kw')
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element(By.ID,'kw').send_keys('tom')