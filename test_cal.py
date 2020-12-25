import unittest
import calcul

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calcul.add(10,5), 15)
        self.assertEqual(calcul.add(20,5), 25)

    def test_sub(self):
        self.assertEqual(calcul.subtract(10,5), 5)
        self.assertEqual(calcul.subtract(45, 2), 43)

    def test_mul(self):
        self.assertEqual(calcul.multiply(8, 5), 40)
        self.assertEqual(calcul.multiply(7,7), 49)

    def test_div(self):
        self.assertEqual(calcul.divide(5,2), 2.5)
        self.assertEqual(calcul.divide(9,3), 3)
        self.assertEqual(calcul.divide(10,0), 0)
        
        """
        with self.assertRaises(ValueError):
            calcul.divide(10,0)
        """

if __name__ == '__main__':
    unittest.main()