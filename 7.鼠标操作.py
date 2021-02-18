#author:malei
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Chrome('c://driver/chromedriver.exe')
dr.get('https://www.baidu.com')
set_element = dr.find_element_by_id('s-usersetting-top')
ActionChains(dr).move_to_element()
ActionChains(dr).double_click(set_element)
ActionChains(dr).context_click(set_element)