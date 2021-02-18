#author:malei
# 测试套件

import unittest

class Testdemo1(unittest.TestCase):
	def test_login(self):
		print('aaa')
	
	def test_exit(self):
		print(0)
		
		
class Testdemo2(unittest.TestCase):
	@unittest.skip
	def test_login(self):
		print(1)
	def test_exit(self):
		print(0)
		
if __name__ == '__main__':
    # suit = unittest.TestSuite([Testdemo1('test_login'),Testdemo2('test_login')])
    # unittest.TextTestRunner().run(suit)
    
    # suit1 = unittest.TestLoader().loadTestsFromTestCase(Testdemo1)
    # suit2 = unittest.TestLoader().loadTestsFromTestCase(Testdemo2)
    # suit = [suit1,suit2]
    # unittest.TextTestRunner().run(unittest.TestSuite(suit))
    
    suit = unittest.defaultTestLoader.discover('./','test*.py')
    unittest.TextTestRunner().run(suit)
    