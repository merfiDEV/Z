import os
print("сделано By merfiDEV/Maked by MerfiDEV")
def find_file(file_name, search_directory):
    for root, dirs, files in os.walk(search_directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Файл {file_path} был успешно удален.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

def main():
    file_name = input("Введите название файла для поиска: ")
    search_directory = '/storage/emulated/0'

    file_path = find_file(file_name, search_directory)

    if file_path:
        print(f"Файл найден по пути: {file_path}")
        choice = input("Вы хотите удалить этот файл? (1 - удалить, 0 - отменить): ")

        if choice == '1':
            confirm = input("Вы уверены, что хотите удалить этот файл? (1 - подтвердить, 0 - отменить): ")
            if confirm == '1':
                delete_file(file_path)
            else:
                print("Удаление отменено.")
        else:
            print("Удаление отменено.")
    else:
        print("Файл не найден.")

if __name__ == "__main__":
    main()
