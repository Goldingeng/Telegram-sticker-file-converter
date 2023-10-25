import os
import uuid

def generate_random_filename():
    return str(uuid.uuid4())[:8]

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n' * 100)

desired_size = (512, 512)

src_folder = 'src/data'

result_folder = "src\\result" 