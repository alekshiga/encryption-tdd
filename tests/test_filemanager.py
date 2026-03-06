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


if __name__ == "__main__":
    unittest.main()