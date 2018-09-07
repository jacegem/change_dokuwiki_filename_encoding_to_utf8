import os
from glob import glob
import urllib.parse


def change_file(path):
    files = glob(path, recursive=True)
    for file in files:
        if os.path.isfile(file):
            dir_name = os.path.dirname(file)
            file_name = os.path.basename(file)
            print('{} and {}'.format(dir_name, file_name))
            new_name = urllib.parse.unquote(file_name)
            print("encode to {}".format(new_name))
            os.rename(os.path.join(dir_name, file_name), os.path.join(dir_name, new_name))


def change_folder(path):
    files = glob(path, recursive=True)
    for file in files:
        if os.path.isdir(file):
            new_name = urllib.parse.unquote(file)
            print("encode to {}".format(new_name))
            os.rename(file, new_name)


if __name__ == "__main__":
    base_folder = '/Users/jace/Workspace/python/pages'
    change_file(base_folder + '/**/*.txt')
    change_folder(base_folder + '/**/')
