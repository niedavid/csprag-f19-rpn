import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 1 -")
        self.assertEqual(4, result)
    def test_multiply(self):
        result = rpn.calculate("3 3 *")
        self.assertEqual(9, result)
    def test_div1(self):
        result = rpn.calculate('12 8 /')
        self.assertEqul(1, result)
    def test_div2(self):
        result = rpn.calculate('24 8 /')
        self.assertEqul(3, result)
    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')

#EOF
