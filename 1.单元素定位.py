#author:malei

from selenium import webdriver

driver = webdriver.Chrome(r"C:\driver\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.maximize_window()
# element_input = driver.find_element_by_id("kw")
# element_input = driver.find_element_by_xpath("//input[@id='kw']")
element_input = driver.find_element_by_css_selector('input#kw')
element_input.send_keys("hello")
# driver.quit()
# driver.close()
