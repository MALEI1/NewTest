#author:malei
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

dr = webdriver.Chrome('c://driver/chromedriver.exe')
dr.get('file:///C:/app/test/hello.html')
sel_js = 'document.getElementById("s1").style.display="block";'
dr.execute_script(sel_js)
time.sleep(2)
element = dr.find_element_by_id('s1')
Select(element).select_by_index(2)
time.sleep(5)
dr.quit()
