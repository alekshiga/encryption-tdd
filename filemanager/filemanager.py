from pathlib import Path

class FileManager:

    def __init__(self, encryption):
        self.encryption = encryption

    def encrypt_file(self, path):
        path = Path(path)
        content = path.read_text(encoding="utf-8")
        encrypted_content = self.encryption.encrypt(content)
        encrypted_path = path.with_suffix(path.suffix + ".encrypted")
        encrypted_path.write_text(encrypted_content, encoding="utf-8")

    def decrypt_file(self, path):
        path = Path(path)
        if path.suffix != ".encrypted":
            raise ValueError("Файл должен иметь .encrypted расширение")
        encrypted_content = path.read_text(encoding="utf-8")
        decrypted_content = self.encryption.decrypt(encrypted_content)
        original_file = path.parent / path.stem
        original_file.write_text(decrypted_content, encoding="utf-8")