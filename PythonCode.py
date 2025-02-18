import os
import shutil

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("Folder created successfully.")
    else:
        print("Folder already exists.")

def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print("Folder deleted successfully.")
    else:
        print("Folder does not exist.")

def create_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("This is a test file.")
            print("File created successfully.")
    else:
        print("File already exists.")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

def move_file(file_path, destination_folder_path):
    if os.path.exists(file_path):
        create_folder(destination_folder_path)
        shutil.move(file_path, destination_folder_path)
        print("File moved successfully.")
    else:
        print("File does not exist.")

def copy_file(file_path, destination_folder_path):
    if os.path.exists(file_path):
        create_folder(destination_folder_path)
        shutil.copy(file_path, destination_folder_path)
        print("File copied successfully.")
    else:
        print("File does not exist.")

def rename_file(file_path, new_file_name):
    if os.path.exists(file_path):
        file_directory = os.path.dirname(file_path)
        new_file_path = os.path.join(file_directory, new_file_name)
        os.rename(file_path, new_file_path)
        print("File renamed successfully.")
    else:
        print("File does not exist.")

# create a folder
folder_path = 'C:/example_folder'
create_folder(folder_path)

# create a file
file_path = 'C:/example_folder/example.txt'
create_file(file_path)

# move a file
destination_folder_path = 'C:/example_destination_folder'
move_file(file_path, destination_folder_path)

# copy a file
destination_folder_path = 'C:/example_copy_destination_folder'
copy_file(file_path, destination_folder_path)

# rename a file
new_file_name = 'example_renamed.txt'
rename_file(file_path, new_file_name)

# delete a file
delete_file(os.path.join(destination_folder_path, new_file_name))

# delete a folder
delete_folder(folder_path)
