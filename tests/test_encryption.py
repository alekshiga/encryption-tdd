import unittest
from encryption.encryption import Encryption


class TestEncryption(unittest.TestCase):

    def test_encrypt_shifts_letters_by_one(self):
        encryption = Encryption()
        result = encryption.encrypt("abc")
        self.assertEqual(result, "bcd")

    def test_decrypt_shifts_letters_back(self):
        encryption = Encryption()
        result = encryption.decrypt("bcd")
        self.assertEqual(result, "abc")

if __name__ == "__main__":
    unittest.main()