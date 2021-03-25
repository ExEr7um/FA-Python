import os
import shutil
import json

settings = {}
root_path = ""


# Проверка существования директории
def exists(name):
    if os.path.exists(f"{path}/{name}"):
        return True
    else:
        return False


# Проверка нахождения пути в домашней папке
def in_root(path):
    global root_path
    if os.path.relpath(path, root_path)[:2] != "..":
        return True
    else:
        return False


# 1. Сменить директорию
def cd():
    global path, root_path
    new_path = input("\r\nВведите новый путь: ")
    if os.path.isabs(new_path) and os.path.exists(new_path) and in_root(f"{path}/{new_path}"):
        if in_root(new_path):
            path = new_path
            print("\r\nУспешно!")
        else:
            print(
                f"Вы не можете выходить за пределы домашней папки: {root_path}")
    elif exists(new_path) and in_root(f"{path}/{new_path}"):
        path = f"{path}/{new_path}"
    elif not in_root(f"{path}/{new_path}"):
        print(f"Вы не можете выходить за пределы домашней папки: {root_path}")
    else:
        print("Папки не существует!")


# 2. Список файлов
def ls():
    global path, root_path
    for file in os.listdir(path):
        if file[0] != ".":
            print(file)
    print("\r\nУспешно!")


# 3. Создать папку
def mkdir():
    global path
    dir_name = input("\r\nВведите название папки: ")
    if exists(dir_name):
        print("Папка уже существует!")
    else:
        os.mkdir(f"{path}/{dir_name}")
        print("\r\nУспешно!")


# 4. Удалить папку
def rmdir():
    global path
    dir_name = input("\r\nВведите название папки: ")
    if exists(dir_name):
        os.rmdir(f"{path}/{dir_name}")
        print("\r\nУспешно!")
    else:
        print("Папки не существует!")


# 5. Создать файл
def create():
    global path
    file_name = input("\r\nВведите название файла: ")
    if exists(file_name):
        print("Файл уже существует!")
    else:
        open(f"{path}/{file_name}", "x").close()
        print("\r\nУспешно!")


# 6. Переименовать файл
def rename():
    global path
    old_name = input("\r\nВведите старое название файла: ")
    if exists(old_name):
        new_name = input("\r\nВведите новое название файла: ")
        if exists(new_name):
            print("Файл уже существует!")
        else:
            os.rename(f"{path}/{old_name}", f"{path}/{new_name}")
            print("\r\nУспешно!")
    else:
        print("Файла не существует!")


# 7. Прочитать файл
def read():
    global path
    file_name = input("\r\nВведите название файла: ")
    if exists(file_name):
        file = open(f"{path}/{file_name}")
        for line in file.readlines():
            print(line)
        file.close()
        print("\r\nУспешно!")
    else:
        print("Файла не существует!")


# 8. Удалить файл
def remove():
    global path
    file_name = input("\r\nВведите название файла: ")
    if exists(file_name):
        os.remove(f"{path}/{file_name}")
        print("\r\nУспешно!")
    else:
        print("Файла не существует!")


# 9. Скопировать файл
def copy():
    global path, root_path
    file_name = input("\r\nВведите название файла: ")
    if exists(file_name):
        copy_path = input("\r\nВведите путь для копирования: ")
        if os.path.isabs(copy_path):
            if in_root(copy_path):
                if os.path.exists(f"{copy_path}/{file_name}"):
                    print("Файл уже существует!")
                else:
                    shutil.copy(f"{path}/{file_name}", copy_path)
                    print("\r\nУспешно!")
            else:
                print(
                    f"Вы не можете выходить за пределы домашней папки: {root_path}")
        else:
            print("Вы должны ввести абсолютный путь!")
    else:
        print("Файла не существует!")


# 10. Переместить файл
def move():
    global path, root_path
    file_name = input("\r\nВведите название файла: ")
    if exists(file_name):
        move_path = input("\r\nВведите путь для перемещения: ")
        if os.path.isabs(move_path):
            if in_root(move_path):
                if os.path.exists(f"{move_path}/{file_name}"):
                    print("Файл уже существует!")
                else:
                    shutil.move(f"{path}/{file_name}", move_path)
                    print("\r\nУспешно!")
            else:
                print(
                    f"Вы не можете выходить за пределы домашней папки: {root_path}")
        else:
            print("Вы должны ввести абсолютный путь!")
    else:
        print("Файла не существует!")


# 11. Записать в файл
def write():
    global path
    file_name = input("\r\nВведите название файла: ")
    if exists(file_name):
        input_text = input("\r\nВведите текст: ")
        with open(f"{path}/{file_name}", "w") as file:
            file.write(input_text)
        print("\r\nУспешно!")
    else:
        print("Файла не существует!")


# 12. Изменить домашнюю директорию
def set_root_path():
    global root_path, settings, path
    root_path = input("Введите домашнюю директорию: ")
    settings["rootPath"] = root_path
    with open("Настройки.json", "w") as settings_file:
        json.dump(settings, settings_file)
    path = root_path
    print("\r\nУспешно!")


commands = {
    # 1. Сменить директорию
    "1": cd,
    "cd": cd,
    # 2. Список файлов
    "2": ls,
    "ls": ls,
    # 3. Создать папку
    "3": mkdir,
    "mkdir": mkdir,
    # 4. Удалить папку
    "4": rmdir,
    "rmdir": rmdir,
    # 5. Создать файл
    "5": create,
    "create": create,
    "touch": create,
    # 6. Переименовать файл
    "6": rename,
    "rename": rename,
    # 7. Прочитать файл
    "7": read,
    "read": read,
    "cat": read,
    # 8. Удалить файл
    "8": remove,
    "remove": remove,
    "delete": remove,
    "rm": remove,
    # 9. Скопировать файл
    "9": copy,
    "copy": copy,
    "cp": copy,
    # 10. Переместить файл
    "10": move,
    "move": move,
    "mv": move,
    # 11. Записать в файл
    "11": write,
    # 12. Изменить домашнюю директорию
    "12": set_root_path,
}

try:
    with open("Настройки.json") as settings_file:
        settings = json.load(settings_file)
    if settings["rootPath"]:
        root_path = settings["rootPath"]
    else:
        raise FileNotFoundError
except FileNotFoundError:
    set_root_path()

path = root_path

while True:
    print(
        "\r\n\033[1mДОСТУПНЫЕ КОМАНДЫ\033[0m\r\n1. Сменить директорию\r\n2. Список файлов\r\n3. Создать папку\r\n4. Удалить папку\r\n5. Создать файл\r\n6. Переименовать файл\r\n7. Прочитать файл\r\n8. Удалить файл\r\n9. Скопировать файл\r\n10. Переместить файл\r\n11. Записать в файл\r\n12. Изменить домашнюю директорию")
    command = input(
        f"\r\nТекущая директория: {path}\r\nВыберите команду: ").split()
    commands[command[0]]()
