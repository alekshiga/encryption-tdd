class Encryption:

    def __init__(self):
        # сделаем заглушку чтобы проходил тест
        pass

    # приватный метод для сдвига todo что-нибудь посложнее потом можно будет придумать
    @staticmethod
    def _shift(char, shift):
        if char.isupper():
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        return char

    def encrypt(self, text, shift):
        result = [self._shift(char, shift) for char in text]
        return ''.join(result)

    def decrypt(self, text, shift):
        # расшифровка шифра
        return self.encrypt(text, 26 - (shift % 26))