import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encryption.encryption import Encryption

class TestEncryption(unittest.TestCase):

    def test_class_creation(self):
        encryption = Encryption()
        self.assertIsNotNone(encryption)

if __name__ == '__main__':
    unittest.main()