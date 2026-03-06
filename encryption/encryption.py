class Encryption:

    def encrypt(self, text):
        result = ""
        for c in text:
            if 'a' <= c <= 'y' or 'A' <= c <= 'Y':
                result += chr(ord(c) + 1)
            elif c == 'z':
                result += 'a'
            elif c == 'Z':
                result += 'A'
            elif '0' <= c <= '8':
                result += chr(ord(c) + 1)
            elif c == '9':
                result += '0'
            else:
                result += c
        return result

    def decrypt(self, text):
        result = ""
        for c in text:
            if 'b' <= c <= 'z' or 'B' <= c <= 'Z':
                result += chr(ord(c) - 1)
            elif c == 'a':
                result += 'z'
            elif c == 'A':
                result += 'Z'
            elif '1' <= c <= '9':
                result += chr(ord(c) - 1)
            elif c == '0':
                result += '9'
            else:
                result += c
        return result