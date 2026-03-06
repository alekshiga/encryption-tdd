import unittest
import tempfile
from pathlib import Path

from filemanager.filemanager import FileManager
from encryption.encryption import Encryption


class TestFileManager(unittest.TestCase):

    def test_encrypt_file_creation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "test.txt"
            file_path.write_text("abc")
            manager = FileManager(Encryption())
            manager.encrypt_file(file_path)
            encrypted_file = Path(tmpdir) / "test.txt.encrypted"
            self.assertTrue(encrypted_file.exists())

    def test_file_decryption(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            encrypted_file = Path(tmpdir) / "data.txt.encrypted"
            encrypted_file.write_text("bcd")
            manager = FileManager(Encryption())
            manager.decrypt_file(encrypted_file)
            result_file = Path(tmpdir) / "data.txt"
            self.assertTrue(result_file.exists())

    # тест на корректного восстанавление файла
    def test_decrypt_file_restores_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            encrypted_file = Path(tmpdir) / "data.txt.encrypted"
            encrypted_file.write_text("bcd")

            manager = FileManager(Encryption())
            manager.decrypt_file(encrypted_file)

            original_file = Path(tmpdir) / "data.txt"
            content = original_file.read_text()
            self.assertEqual(content, "abc")

if __name__ == "__main__":
    unittest.main()