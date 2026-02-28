import os

# проверка папки на существование
def is_valid_directory(path):
    return os.path.isdir(path)

# получаем файлы которые можно зашифровать/расшифровать
def get_filtered_files(directory, command):
    files = []

    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)

        if not os.path.isfile(full_path):
            continue

        if command == "encrypt" and not file.endswith(".encrypted"):
            files.append(file)

        if command == "decrypt" and file.endswith(".encrypted"):
            files.append(file)

    return files

# при шифровании файл получает расширение .encrypted
def build_output_filename(directory, filename, command):
    if command == "encrypt":
        return os.path.join(directory, filename + ".encrypted")

    if command == "decrypt":
        if filename.endswith(".encrypted"):
            filename = filename.replace(".encrypted", ".decrypted")
        else:
            filename = filename + ".decrypted"

        return os.path.join(directory, filename)

    raise ValueError("Unknown command")