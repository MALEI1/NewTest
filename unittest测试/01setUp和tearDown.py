#author:malei
import unittest
from selenium import webdriver


class TestWeb(unittest.TestCase):
	def setUp(self) -> None:
		self.dr = webdriver.Chrome('C:/driver/chromedriver.exe')

	def tearDown(self) -> None:
		self.dr.quit()
		
	def test_QQLogin(self):
		self.dr.get('https://mail.qq.com/')
		self.assertEqual(self.dr.title,'登录QQ邮箱',msg='页面跳转失败')
	# @unittest.skip
	def test_MaoyanMOvie(self):
		self.dr.get('https://maoyan.com')
		self.assertEqual(self.dr.title,'电影院票房购票_评分_选座_经典影视推荐-猫眼电影',msg='页面跳转失败')

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestWeb("test_QQLogin"))
    unittest.TextTestRunner().run(suit)
