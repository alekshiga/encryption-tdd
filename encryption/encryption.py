class Encryption:

    def __init__(self):
        # сделаем заглушку чтобы проходил тест
        pass

    def encrypt(self, text, shift):
        # обычный сдвиг шифром Цезаря, todo сделать что-нибудь посложнее
        result = []
        for char in text:
            if char.isupper():
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            elif char.islower():
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)