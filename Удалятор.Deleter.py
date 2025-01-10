import os
print("\033[34mSuccefuly started\033[0m")
print("\033[32mСделано By MerfiDEV/Maked by MerfiDEV\033[0m")

def find_files(partial_name, search_directory):
    matching_files = []
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if partial_name in file:
                matching_files.append(os.path.join(root, file))
    return matching_files

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Файл {file_path} был успешно удален.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

def main():
    search_directory = '/storage/emulated/0'
    
    while True:
        partial_name = input("Введите часть, или полное имя файла для поиска: ")
        matching_files = find_files(partial_name, search_directory)

        if matching_files:
            print("Найдены файлы:")
            for i, file_path in enumerate(matching_files, 1):
                print(f"{i}: {file_path}")
            
            choice = input("Введите номер файла для удаления или 0 для отмены: ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(matching_files):
                    selected_file = matching_files[choice - 1]
                    confirm = input(f"Вы уверены, что хотите удалить {selected_file}? (1 - подтвердить, 0 - отменить): ")
                    if confirm == '1':
                        delete_file(selected_file)
                    else:
                        print("Удаление отменено.")
                elif choice == 0:
                    print("Удаление отменено.")
                else:
                    print("Некорректный выбор.")
            else:
                print("Некорректный ввод.")
            break
        else:
            print("Файлы не найдены. Попробуйте снова.")

if __name__ == "__main__":
    main()
