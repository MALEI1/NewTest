#author:malei

import time
# 强制等待
time.sleep(2)
# 隐式等待
from selenium import webdriver

dr = webdriver.Chrome('c:/driver/chromedriver.exe')
dr.implicitly_wait(30)
# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(dr,5,0.5).until()