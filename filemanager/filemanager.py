from pathlib import Path


class FileManager:

    def __init__(self, encryption):
        self.encryption = encryption

    def encrypt_file(self, path):
        new_file = str(path) + ".encrypted"
        Path(new_file).touch()