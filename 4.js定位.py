#author:malei

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/driver/chromedriver.exe')
driver.get('https://www.baidu.com')
driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('hello')
js_button = 'document.getElementById("su").click();'
driver.execute_script(js_button)

time.sleep(2)
driver.quit()

