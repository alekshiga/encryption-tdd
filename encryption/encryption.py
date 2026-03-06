# encryption/encryption.py
class Encryption:
    def __init__(self, shift=1):
        self.shift = shift

    def encrypt(self, text):
        result = ""
        for c in text:
            if 'a' <= c <= 'z':
                result += chr((ord(c) - ord('a') + self.shift) % 26 + ord('a'))
            elif 'A' <= c <= 'Z':
                result += chr((ord(c) - ord('A') + self.shift) % 26 + ord('A'))
            elif '0' <= c <= '9':
                result += chr((ord(c) - ord('0') + self.shift) % 10 + ord('0'))
            else:
                result += c
        return result

    def decrypt(self, text):
        result = ""
        for c in text:
            if 'a' <= c <= 'z':
                result += chr((ord(c) - ord('a') - self.shift) % 26 + ord('a'))
            elif 'A' <= c <= 'Z':
                result += chr((ord(c) - ord('A') - self.shift) % 26 + ord('A'))
            elif '0' <= c <= '9':
                result += chr((ord(c) - ord('0') - self.shift) % 10 + ord('0'))
            else:
                result += c
        return result