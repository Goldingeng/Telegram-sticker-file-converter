from PIL import Image
import os
from config import generate_random_filename

def resize_image(image, max_size):
    width, height = image.size
    if width <= max_size and height <= max_size:
        return image

    if width > height:
        new_width = max_size
        new_height = int(max_size * (height / width))
    else:
        new_height = max_size
        new_width = int(max_size * (width / height))

    return image.resize((new_width, new_height), Image.LANCZOS)

def static_sticker(src_folder, result_folder, max_size=512):
    for filename in os.listdir(src_folder):
        print(f"Processing: {filename}")
        img = Image.open(os.path.join(src_folder, filename))
        img = resize_image(img, max_size)
        img.save(os.path.join(result_folder, generate_random_filename() + '.png'), 'png')
    print("Completed!")
