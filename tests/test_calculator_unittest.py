import unittest

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        real = add(2,4)
        expect = 6
        self.assertEqual(real, expect)
        
    def test_subtraction(self):
        real = sub(2,4)
        expect = -2
        self.assertEqual(real, expect)
        
    def test_multiplication(self):
        real = mul(2,4)
        expect = 8
        self.assertEqual(real, expect)
        
    def test_division(self):
        real = div(4,2)
        expect 2
        self.assertEqual(real, expect)
        
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            div(4,0)
            
        self.assertTrue('ZeroDivisionError: division by zero' in str(context.exception))
        
if __name__ == '__main__':
    unittest.main()
        
