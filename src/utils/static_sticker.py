from PIL import Image
import os
import uuid
import config

def generate_random_filename():
    return str(uuid.uuid4())[:8]

def static_sticker(src_folder, result_folder):
    for filename in os.listdir(src_folder):
        img = Image.open(os.path.join(src_folder, filename))
        img = img.resize(config.desired_size, Image.LANCZOS)
        img.save(os.path.join(result_folder, generate_random_filename() + '.webp'), 'webp')
    print("Completed!")