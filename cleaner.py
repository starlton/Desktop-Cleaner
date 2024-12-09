import os
import shutil


def autosort_files(desktop_dir, target_folder, file_type):
    target_path = os.path.join(desktop_dir, target_folder)


    if not os.path.isdir(target_path):
        os.makedirs(target_path)

    all_items = os.listdir(desktop_dir)

    for item in all_items:
        if item.endswith(file_type):
            source_path = os.path.join(desktop_dir, item)
            destination = os.path.join(target_path, item)
            if not os.path.exists(destination):
                print(f"Moving {item} to {target_path}")
                shutil.move(source_path, target_path)
            else:
                print(f"File {item} already exists in {target_path}")


def clean_up_desktop(desktop_dir):
    predefined_folders = ["Documents", "Images", "Videos"]
    for folder in predefined_folders:
        folder_dir = os.path.join(desktop_dir, folder)
        if not os.path.isdir(folder_dir):
            os.makedirs(folder_dir)

    for item in os.listdir(desktop_dir):
        source_path = os.path.join(desktop_dir, item)
        if os.path.isfile(source_path):
            folder = file_type(item)

            if folder:
                folder_dir = os.path.join(desktop_dir, folder)
                unique_name = item
                counter = 1

                while os.path.exists(os.path.join(folder_dir, unique_name)):
                    name, ext = os.path.splitext(item)
                    unique_name = f"{name}_{counter}{ext}"
                    counter += 1

                print(f"Moving {item} to {os.path.join(folder_dir, unique_name)}")
                shutil.move(source_path, os.path.join(folder_dir, unique_name))


def file_type(file_name):
    img_types = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    vid_types = ['.mp4', '.avi', '.mkv', '.mov']
    doc_types = ['.txt', '.docx', '.pdf', '.xlsx']

    file_ext = os.path.splitext(file_name)[1].lower()

    if file_ext in img_types:
        return 'Images'
    elif file_ext in vid_types:
        return 'Videos'
    elif file_ext in doc_types:
        return 'Documents'
    else:
        return None



desktop_directory = r"C:\users\st567793\OneDrive - Loras College\desktop"

user = input("Do you want to auto-arrange the desktop? (yes/no): ").lower()
if user == "yes":
    clean_up_desktop(desktop_directory)
else:
    file_extension = input("Enter the format of the file you want to sort: ")
    folder_name = input("Enter the destination folder: ")
    autosort_files(desktop_directory, folder_name, file_extension)




