import os
from encryption import Encryption
from file_manager.manager import (
    is_valid_directory,
    get_filtered_files,
    build_output_filename
)

def get_command():
    while True:
        print("1. Зашифровать файл")
        print("2. Расшифровать файл")
        print("3. Выйти")

        command = input("Выберите команду: ").strip()

        if command in ["1", "encrypt"]:
            return "encrypt"
        elif command in ["2", "decrypt"]:
            return "decrypt"
        elif command in ["3", "exit", "quit", "q"]:
            return "exit"
        else:
            print("Неверная команда\n")


def get_directory():
    while True:
        directory = input("Введите путь к папке (Без кавычек): ").strip()

        if not is_valid_directory(directory):
            print("Папка не существует\n")
            continue

        return directory


def choose_file(files):
    if not files:
        print("Нет доступных файлов")
        return None

    print("\nДоступные файлы:")
    for index, file in enumerate(files, 1):
        print(f"{index}. {file}")

    while True:
        choice = input("Введите номер файла: ").strip()

        try:
            index = int(choice) - 1
            if 0 <= index < len(files):
                return files[index]
            else:
                print("Неверный номер")
        except ValueError:
            print("Введите число")


def get_shift():
    while True:
        try:
            return int(input("Введите сдвиг: ").strip())
        except ValueError:
            print("Сдвиг должен быть числом")


def main():
    print("ШИФРАТОР / ДЕШИФРАТОР")

    command = get_command()
    if command == "exit":
        return

    directory = get_directory()

    files = get_filtered_files(directory, command)
    filename = choose_file(files)

    if not filename:
        return

    shift = get_shift()

    encryption = Encryption()

    input_path = os.path.join(directory, filename)
    content = encryption.read_file(input_path)

    if not content:
        print("Файл пуст или не удалось прочитать")
        return

    if command == "encrypt":
        result = encryption.encrypt(content, shift)
    else:
        result = encryption.decrypt(content, shift)

    output_path = build_output_filename(directory, filename, command)

    if encryption.write_file(output_path, result):
        print(f"Файл сохранён: {output_path}")
    else:
        print("Ошибка при сохранении файла")


if __name__ == "__main__":
    main()