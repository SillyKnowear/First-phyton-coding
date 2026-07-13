import os
import shutil

folder_path = 'C:/Users/msan1/Downloads'  # Replace with the path to your Downloads folder. Meaning replace (msan1) with your downlaod for the code to work.

files = os.listdir(folder_path)

for file in files:
    if '.' in file:
        extension = file.split('.')[-1]
        print(file, '->', extension)

        new_folder = os.path.join(folder_path, extension)

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(new_folder, file)

        shutil.move(old_path, new_path)
        print(f'Moved {file} to {extension} folder.')

