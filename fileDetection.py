import os

file_path = "bankingSystem.py"

if os.path.exists(file_path):
    print(f"{file_path} exists")
    
    if os.path.isfile(file_path):
        print(f"that is a file!")
    elif os.path.isdir(file_path):
        print(f"that is a directory!")
    else:
        print(f"{file_path} is not a file neither a directory")
else:
    print(f"{file_path} does not exist")