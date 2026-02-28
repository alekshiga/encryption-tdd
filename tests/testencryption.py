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

    # write_file должен создавать файл
    def test_write_file_creates_file(self):
        encryption = Encryption()
        test_file = os.path.join("test.txt")
        test_content = "Hello"
        result = encryption.write_file(test_file, test_content)
        self.assertTrue(result)  # должно вернуть True
        self.assertTrue(os.path.exists(test_file))  # файл должен существовать после выполнения функции

    # write_file должен правильно ожидаемо записывать содержимое
    def test_write_file_writes_correct_content(self):
        encryption = Encryption()
        test_file = os.path.join("test.txt")
        test_content = "Hello"
        encryption.write_file(test_file, test_content)
        with open(test_file, 'r', encoding='utf-8') as f:
            written_content = f.read()
        self.assertEqual(written_content, test_content)

    # read_file должен вернуть None если файл не существует
    def test_read_file_returns_none_for_nonexistent_file(self):
        encryption = Encryption()
        nonexistent_file = os.path.join("does_not_exist.txt")
        content = encryption.read_file(nonexistent_file)
        self.assertIsNone(content)

if __name__ == '__main__':
    unittest.main()