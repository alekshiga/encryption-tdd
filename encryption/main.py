import sys
import os
from encryption import Encryption

def get_filename():
    while True:
        filename = input("Введите имя файла: ").strip()

        if not filename:
            print("Имя файла не может быть пустым")
            continue
            # Проверяем существование файла

        if not os.path.exists(filename):
            print(f"Файл '{filename}' не найден")
            print("Введите другое название файла")
            continue

        return filename

def get_shift():
    while True:
        try:
            shift = input("Введите сдвиг: ").strip()
            shift = int(shift)
            return shift
        except ValueError:
            print("Сдвиг должен быть целым числом")


def get_command():
    while True:
        print("1. Зашифровать файл")
        print("2. Расшифровать файл")
        print("3. Выйти из программы")
        command = input()

        if command in ['1', 'encrypt']:
            return 'encrypt'
        elif command in ['2', 'decrypt']:
            return 'decrypt'
        elif command in ['3', 'exit', 'quit', 'q']:
            return 'exit'
        else:
            print("Неверная команда, попробуйте снова")

def main():

    print("ШИФРАТОР/ДЕШИФРАТОР ФАЙЛОВ")

    encryption = Encryption()

    input_file = get_filename()

    command = get_command()
    if command == 'exit':
        return

    shift = get_shift()

    print(f"Чтение файла: {input_file}")
    content = encryption.read_file(input_file)
    if content is None:
        print("Входной файл пуст")
        return

    if command == 'encrypt':
        print("Шифруем файл...")
        result = encryption.encrypt(content, shift)
        output_file = f"{input_file}.encrypted"

    elif command == 'decrypt':
        print("Расшифровка файла...")
        result = encryption.decrypt(content, shift)

        output_file = input_file.replace(".encrypted", ".decrypted")
        if output_file == input_file:
            output_file = f"{input_file}.decrypted"
    else:
        print(f"Неизвестная команда {command}")
        return

    if encryption.write_file(output_file, result):
        print("Успешно")
    else:
        print("Не удалось сохранить результат")

if __name__ == "__main__":
    main()