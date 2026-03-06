import unittest
from encryption.encryption import Encryption


class TestEncryption(unittest.TestCase):

    def test_encrypt(self):
        encryption = Encryption()
        result = encryption.encrypt("abc")
        self.assertEqual(result, "bcd")

    def test_decrypt(self):
        encryption = Encryption()
        result = encryption.decrypt("bcd")
        self.assertEqual(result, "abc")

if __name__ == "__main__":
    unittest.main()