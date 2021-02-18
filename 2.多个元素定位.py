#author:malei
from selenium import webdriver

driver = webdriver.Chrome("C://driver//chromedriver.exe")
driver.get("https://www.baidu.com")
tag = driver.find_elements_by_tag_name('input')
for t in tag:
	if t.get_attribute('autocomplete') =='off':
		t.send_keys('tom')

driver.find_element_by_id('su').click()
driver.quit()