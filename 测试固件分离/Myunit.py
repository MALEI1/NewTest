#author:malei
import unittest
from selenium import  webdriver

class Myunit(unittest.TestCase):
	def setUp(self) -> None:
		self.dr = webdriver.Chrome('C:/driver/chromedriver.exe')
		
	def tearDown(self) -> None:
		self.dr.quit()
		
