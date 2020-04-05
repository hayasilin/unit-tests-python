import unittest
from module import Calculator

class ModuleTest(unittest.TestCase):
	def setUp(self):
		self.calculator = Calculator(8, 4)

	def tearDown(self):
		pass

	def test_add(self):
		result = self.calculator.add()
		self.assertEqual(result, 12)

	def test_subtract(self):
		result = self.calculator.subtract()
		self.assertEqual(result, 4)

	def test_multiple(self):
		result = self.calculator.multiple()
		self.assertEqual(result, 32)

	def test_divide(self):
		result = self.calculator.divide()
		self.assertEqual(result, 2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_subtract"))
    suite.addTest(ModuleTest("test_multiple"))
    suite.addTest(ModuleTest("test_divide"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
