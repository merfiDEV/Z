import os
import requests

file_name = "Удалятор.Deleter.py"
download_url = "https://raw.githubusercontent.com/merfiDEV/Z/main/Удалятор.Deleter.py"
save_path = f"/storage/emulated/0/merfiDEV/{file_name}" 

languages = {
    1: {
        "searching": "Ищем и удаляем старые версии файла...",
        "downloading": "Скачиваем новую версию файла...",
        "deleted": "Удалён файл: ",
        "permission_error": "Ошибка доступа при удалении: ",
        "download_success": "Обновление завершено!",
        "download_fail": "Ошибка при обновлении файла!",
        "download_path": "*Успешно завершено, Обнова по пути: ",
    },
    2: {
        "searching": "Searching and deleting old versions of the file...",
        "downloading": "Downloading a new version of the file...",
        "deleted": "Deleted file: ",
        "permission_error": "Permission error while deleting: ",
        "download_success": "Update completed!",
        "download_fail": "Failed to update the file!",
        "download_path": "Successfully completed, update at path: ",
    },
}

def choose_language():
    print("Select a language / Выберите язык:")
    print("1. Russian")
    print("2. English")
    while True:
        try:
            choice = int(input("Your choice / Ваш выбор: "))
            if choice in languages:
                return languages[choice]
            else:
                print("Invalid choice, try again / Неверный выбор, попробуйте снова.")
        except ValueError:
            print("Please enter a number / Введите число.")

def find_and_delete_file(root_path, target_file, messages):
    print(messages["searching"])
    for root, dirs, files in os.walk(root_path):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            try:
                os.remove(file_path)
                print(messages["deleted"] + file_path)
            except PermissionError:
                print(messages["permission_error"] + file_path)

def download_file(url, save_path, messages):
    print(messages["downloading"])
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            return True
        else:
            print(f"HTTP error: {response.status_code}")
            return False
    except Exception as e:
        print(messages["download_fail"], e)
        return False

messages = choose_language()
find_and_delete_file("/storage/emulated/0", file_name, messages)
if download_file(download_url, save_path, messages):
    print(messages["download_success"])
    print(messages["download_path"] + save_path)
else:
    print(messages["download_fail"])
