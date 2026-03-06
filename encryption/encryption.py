class Encryption:

    def encrypt(self, text):
        return "".join(chr(ord(c) + 1) for c in text)

    def decrypt(self, text):
        return "".join(chr(ord(c) - 1) for c in text)