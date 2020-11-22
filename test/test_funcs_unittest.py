import unittest
from snips import funcs_testing

class TestFuncs(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(funcs_testing.hello(), 'hello')

    def test_hello_raises(self):
        with self.assertRaises(ValueError):
            funcs_testing.hello_raises()

if __name__ == '__main__':
    unittest.main()
