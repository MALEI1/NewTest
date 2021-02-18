#author:malei
from 测试固件分离.Myunit import Myunit

import unittest
class TestModel(Myunit):
	def test_baidu(self):
		self.dr.get('https://www.baidu.com')
		self.assertEqual(self.dr.title,'百度一下，你就知道',msg='页面未正常打开')
		
if __name__ == '__main__':
	unittest.main()