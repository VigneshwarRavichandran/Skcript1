from unittest import TestCase

from logic import Logic

class TestLogic(TestCase):
	def test_is_alpha(self):
		logic = Logic("alpha", "alpha")
		self.assertTrue(logic.string1.isalpha())
		self.assertTrue(logic.string2.isalpha())

	def test_example_1(self):
		logic = Logic("edzlatsh", "hazel")
		self.assertTrue(logic.match())

	def test_example_2(self):
		logic = Logic("uwtaqicy", "watch")
		self.assertFalse(logic.match())

	def test_example_3(self):
		logic = Logic("d??????", "code")
		self.assertTrue(logic.match())


	def test_example_4(self):
		logic = Logic("g???", "code")
		self.assertFalse(logic.match())


