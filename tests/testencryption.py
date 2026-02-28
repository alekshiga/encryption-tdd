import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from encryption.encryption import Encryption

class TestEncryption(unittest.TestCase):

    def test_class_creation(self):
        encryption = Encryption()
        self.assertIsNotNone(encryption)

    def test_encryption(self):
        encryption = Encryption()
        result = encryption.encrypt('aaaa', 3)
        # Сейчас используется шифр Цезаря, обычный сдвиг
        # 1 - a, 2 - b, 3 - c, 4 - d
        self.assertEqual(result, 'dddd')

    def test_decryption(self):
        encryption = Encryption()
        encrypted = encryption.encrypt("h", 3)
        decrypted = encryption.decrypt(encrypted, 3)
        self.assertEqual(decrypted, "h")

if __name__ == '__main__':
    unittest.main()