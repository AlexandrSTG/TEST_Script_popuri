import os
import shutil
import json

def copy_non_empty_folders_and_create_json(source_dir, dest_dir, repository_url):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    folder_dict = {}
    
    for file_d in os.walk(source_dir):
        for root, files in os.walk(file_d):
            for file in files:
                if file.lower().endswith('.png'):
                    relative_path = os.path.relpath(root, source_dir)
                    dest_subfolder = os.path.join(dest_dir, relative_path)
                    os.makedirs(dest_subfolder, exist_ok=True)
                    dest_file = os.path.join(dest_subfolder, file)
                    shutil.copy2(os.path.join(root, file), dest_file)

                    # Добавляем путь к файлу в словарь
                    folder_name = os.path.basename(root)
                    if folder_name not in folder_dict:
                        folder_dict[folder_name] = []
                    folder_dict[folder_name].append(os.path.join(repository_url, dest_file[len(dest_dir)+1:].replace('\\', '/')))
                
    # Сохраняем словарь в JSON-файл
    json_file = os.path.join(dest_dir, 'files.json')
    with open(json_file, 'w') as f:
        json.dump(folder_dict, f, indent=4)

if __name__ == "__main__":
    source_folder = 'D:\\TEST_SCRIPT'
    destination_folder = 'D:\\Copy_TEST_SCRIPT'
    repo_url = 'https://github.com/username/repository/blob/main/'

    copy_non_empty_folders_and_create_json(source_folder, destination_folder, repo_url)