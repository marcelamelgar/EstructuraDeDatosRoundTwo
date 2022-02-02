import unidimensionales
import unittest

class TestCode(unittest.TestCase):

    def testingIngreso(self):
        print("hola")
        self.assertEqual(unidimensionales.ingresoDebitos([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22]), [12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22])

if __name__ == '__main__':
    unittest.main()