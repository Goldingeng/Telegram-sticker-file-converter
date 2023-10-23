import os

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n' * 100)

desired_size = (512, 512)
src_folder = 'src/data'