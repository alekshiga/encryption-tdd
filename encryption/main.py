import sys
from pathlib import Path
from filemanager.filemanager import FileManager
from encryption import Encryption


def choose_action():
    while True:
        print("Выберите действие:")
        print("1. Шифровать файл")
        print("2. Дешифровать файл")
        print("3. Выйти из программы")
        choice = input("Выберите: ").strip()
        if choice == "3":
            print("Выход из программы.")
            sys.exit(1)
        if choice in ("1", "2"):
            return choice
        print("Неверный выбор. Попробуйте снова.\n")


def choose_folder():
    while True:
        folder_path = input("Введите путь к папке: ").strip()
        path = Path(folder_path)
        if path.is_dir():
            return path
        print("Папка не найдена. Попробуйте снова.\n")


def choose_file(files):
    while True:
        print("Выберите файл:")
        for idx, f in enumerate(files, start=1):
            print(f"{idx}. {f.name}")
        choice = input(f"Введите число от 1 до {len(files)}: ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return files[idx]
        except ValueError:
            pass
        print("Неверный выбор. Попробуйте снова.\n")


def choose_shift():
    while True:
        shift_input = input("Введите сдвиг для шифра (целое число, по умолчанию 1): ").strip()
        if not shift_input:
            return 1
        try:
            shift = int(shift_input)
            return shift
        except ValueError:
            print("Неверный ввод. Введите целое число.\n")

def main():
    action = choose_action()
    folder = choose_folder()
    shift = choose_shift()
    encryption = Encryption(shift=shift)
    manager = FileManager(encryption)

    if action == "1":
        files = [f for f in folder.iterdir() if f.is_file() and f.suffix != ".encrypted"]
        if not files:
            print("Нет файлов для шифрования")
            return
        file_to_process = choose_file(files)
        manager.encrypt_file(file_to_process)
        print(f"Файл {file_to_process.name} зашифрован с сдвигом {shift}")
    else:
        files = [f for f in folder.iterdir() if f.is_file() and f.suffix == ".encrypted"]
        if not files:
            print("Нет файлов для дешифровки")
            return
        file_to_process = choose_file(files)
        manager.decrypt_file(file_to_process)
        print(f"Файл {file_to_process.name} расшифрован с сдвигом {shift}")

if __name__ == "__main__":
    main()