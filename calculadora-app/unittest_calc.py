from calc_plus import *
import unittest

class Testes(unittest.TestCase):
    def testes_ok(self):
        self.assertEqual (power(2, 5), 32)
        self.assertEqual (log(5,5), 1.0)
        self.assertEqual (square(2), 4)
        print("tudo certo por aqui!")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

if __name__ == '__main__':
    runTests()
