from pathlib import Path


class FileManager:

    def __init__(self, encryption):
        self.encryption = encryption

    def encrypt_file(self, path):
        new_file = str(path) + ".encrypted"
        Path(new_file).touch()

    def decrypt_file(self, path):
        path = Path(path)
        if path.suffix != ".encrypted":
            raise ValueError("Файл должен иметь .encrypted расширение")
        encrypted_content = path.read_text()
        decrypted_content = self.encryption.decrypt(encrypted_content)
        original_file = path.parent / path.stem
        original_file.write_text(decrypted_content)