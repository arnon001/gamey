import os


def find_file():
    path = os.getcwd()
    name = "testfile.txt"

    for root, dirs, files in os.walk(path):
        if name in files:
            file_path = os.path.join(root, name)
            return file_path
        else:
            print("File does not exist")


find_file()
