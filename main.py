import os
from datetime import datetime
from src.utils import animated_sticker, static_sticker
import config

def main():
    src_folder = "src/data"
    result_folder = "src\\result" 
    today = datetime.now().strftime('%Y%m%d')
    try:
        if not os.listdir(src_folder):
            print("Ошибка: Папка data пуста. Загрузите туда исходники")
            return
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return
    while True:
        try:
            name = input("Введите название стикерпака\n>>>")
            date_parts = [today[:4], today[4:6], today[6:]]
            date_folder_name = '.'.join(date_parts)
            new_folder_path = os.path.join(result_folder, f"{name}_{date_folder_name}")
            
            if os.path.exists(new_folder_path):
                print("Папка с таким названием уже существует.")
            else:
                config.clear_screen() 
                break
        except Exception as e:
            print(f"Ошибка: {e}")
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    try:
        os.makedirs(new_folder_path, exist_ok=True)
    except Exception as e:
        print(f"Ошибка: {e}")
    first_file = next(iter(os.listdir(src_folder)), None)
    if first_file and first_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        static_sticker.static_sticker(src_folder, new_folder_path)
    else:
        animated_sticker.animated_sticker(src_folder, new_folder_path)

if __name__ == "__main__":
    main()








