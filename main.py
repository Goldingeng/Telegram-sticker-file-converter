import os
from datetime import datetime
from src.utils import animated_sticker, static_sticker
import config


def main(): 
    src_folder = config.src_folder
    result_folder = config.result_folder
    today = datetime.now().strftime('%Y%m%d')
    try:
        if not os.listdir(src_folder):
            print("Error: The data folder is empty. Please upload source files there.")
            return
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            name = input("Enter the sticker pack name\n>>>")
            date_parts = [today[:4], today[4:6], today[6:]]
            date_folder_name = '.'.join(date_parts)
            new_folder_path = os.path.join(result_folder, f"{name}_{date_folder_name}")
            if os.path.exists(new_folder_path):
                print("A folder with the same name already exists.")
            else:
                config.clear_screen() 
                break
        except Exception as e:
            print(f"Error: {e}")

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    try:
        os.makedirs(new_folder_path, exist_ok=True)
    except Exception as e:
        print(f"Error: {e}")

    first_file = next(iter(os.listdir(src_folder)), None)
    if first_file and first_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        static_sticker.static_sticker(src_folder, new_folder_path)
    else:
        animated_sticker.animated_sticker(src_folder, new_folder_path)
    archive_folder = os.path.join("src", "archive", os.path.basename(new_folder_path))
    try:
        os.makedirs(archive_folder, exist_ok=True)
    except Exception as e:
        print(f"Error creating archive folder: {e}")
    else:

        try:
            for filename in os.listdir(src_folder):
                src_file = os.path.join(src_folder, filename)
                dst_file = os.path.join(archive_folder, filename)
                os.rename(src_file, dst_file)

            for filename in os.listdir(src_folder):
                file_path = os.path.join(src_folder, filename)

                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

        except Exception as e:
            print(f"Error moving files to archive: {e}")


if __name__ == "__main__":
    main()