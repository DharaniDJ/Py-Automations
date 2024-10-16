import os
import shutil

def organize_by_extension(source_folder):
    for filename in os.listdir(source_folder):
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue

        file_extension = filename.split('.')[-1].lower()
        folder_path = os.path.join(source_folder, file_extension)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(os.path.join(source_folder, filename), folder_path)
        print(f"Moved {filename} to {folder_path}")

source_folder = '/path/to/your/folder'
organize_by_extension(source_folder)
