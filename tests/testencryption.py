import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encryption.encryption import Encryption

class TestEncryption(unittest.TestCase):

    def test_class_creation(self):
        encryption = Encryption()
        self.assertIsNotNone(encryption)

    def test_caesar_single_letter_encryption(self):
        encryption = Encryption()
        result = encryption.encrypt('a', 3)
        # 1 - a, 2 - b, 3 - c, 4 - d
        self.assertEqual(result, 'd')

if __name__ == '__main__':
    unittest.main()