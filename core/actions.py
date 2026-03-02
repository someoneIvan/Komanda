import shutil
from pathlib import Path

def change_directory(new_location, current_path):
    if new_location == ".":
        pass
    elif new_location == "..":
        new_location = current_path.parent
    else:
        if Path.is_dir(new_location):
            new_location = current_path / new_location.strip
        elif Path.is_file(new_location):
            print("This is file")
        else:
            print("Unknown error")