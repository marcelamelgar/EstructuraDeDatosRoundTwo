import sumNnumbers
import unittest

class TestCode(unittest.TestCase):

    def testingNumbers(self):
        self.assertEqual(sumNnumbers.sumNnumbers(3), 6)

if __name__ == '__main__':
    unittest.main()