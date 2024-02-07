import unittest
from src import setup
from src.setup import SetupManager

class TestSetup(unittest.TestCase):

    def test_elgamal_key_length(self,key_length):
        setupManager = SetupManager()
        (pk,sk,p,g) = self.setup_elgamal(key_length)
        self.assertEqual(s.bit_length(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        # Code to cleanup after each test
        pass

    def test_initialization(self):
        # Test initialization function
        pass

    def test_database_creation(self):
        # Test database creation function
        pass

    def test_file_creation(self):
        # Test file creation function
        pass

if __name__ == '__main__':
    unittest.main()