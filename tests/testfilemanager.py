import os
import unittest

from file_manager.manager import (
    is_valid_directory,
    get_filtered_files,
    build_output_filename
)


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("data")

        with open(os.path.join(self.test_dir, "file2.encrypted"), "w") as f:
            f.write("data")

        with open(os.path.join(self.test_dir, "file3.txt"), "w") as f:
            f.write("data")

    def tearDown(self):
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_is_valid_directory(self):
        self.assertTrue(is_valid_directory(self.test_dir))
        self.assertFalse(is_valid_directory("non_existing_dir"))

    def test_get_filtered_files_encrypt(self):
        files = get_filtered_files(self.test_dir, "encrypt")

        self.assertIn("file1.txt", files)
        self.assertIn("file3.txt", files)
        self.assertNotIn("file2.encrypted", files)

    def test_get_filtered_files_decrypt(self):
        files = get_filtered_files(self.test_dir, "decrypt")

        self.assertIn("file2.encrypted", files)
        self.assertNotIn("file1.txt", files)
        self.assertNotIn("file3.txt", files)

    def test_build_output_filename_encrypt(self):
        result = build_output_filename(self.test_dir, "file1.txt", "encrypt")
        expected = os.path.join(self.test_dir, "file1.txt.encrypted")
        self.assertEqual(result, expected)

    def test_build_output_filename_decrypt(self):
        result = build_output_filename(self.test_dir, "file2.encrypted", "decrypt")
        expected = os.path.join(self.test_dir, "file2.decrypted")
        self.assertEqual(result, expected)

    def test_build_output_filename_invalid_command(self):
        with self.assertRaises(ValueError):
            build_output_filename(self.test_dir, "file1.txt", "invalid")