import unittest

# This is the class we want to test. So, we need to import it
import Calculator as CalculatorClass

class Test(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):
        result = self.calculator.add(4,8)
        self.assertEquals(result,12)


    def test_0_subtarct(self):
        result = self.calculator.subtarct(4,3)
        self.assertEquals(result,1)

    def test_0_multiply(self):
        result = self.calculator.multiply(4,2)
        self.assertEquals(result, 8)

    def test_0_divide(self):
        result = self.calculator.divide(4,2)
        self.assertEquals(result, 2)
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
    