#author:malei
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
dr = webdriver.Chrome('C:/driver/chromedriver.exe')
dr.get('file:///C:/app/test/hello.html')
element = dr.find_element_by_id('s1')
# Select(element).select_by_value('text1')
# Select(element).select_by_index(2)
Select(element).select_by_visible_text('text4')
time.sleep(5)

dr.quit()