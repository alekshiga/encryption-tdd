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

    # тест работы с цифрами
    def test_encrypt_digits(self):
        encryption = Encryption()
        result = encryption.encrypt("123")
        self.assertEqual(result, "234")

if __name__ == "__main__":
    unittest.main()