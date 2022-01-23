from os import (walk, path, mkdir, remove, rmdir)
from pathlib import (Path)
from sys import (platform)

def scan_in_folder(away):
    for path, _, files in walk("./"):
        if path == away:
            return files

def verify_file(file, factor_validation):

    extension = file.split(".")[len(file.split("."))-1]
    name = "".join(file.split(".")[:-1])

    if extension.upper() == factor_validation.upper():

        return (True, name, extension)

    else:

        return (False, name, extension)

def file_remove(location):
    remove(location)

def folder_remove(location):
    rmdir(location)
    
def convert_url(value):
    
    if platform.upper() == "LINUX":
        return value
    else:
        return "\\".join(value.split("/"))

def file_is_exists(location):
    return Path(location).is_file()

def folder_is_exists(location):
    return path.exists(convert_url(f'{location}'))

def trim(value):
    try:
        return ((value).lstrip()).rstrip()
    except:
        return value


def create_folder(name, location="./"):

    if not path.exists(convert_url(f'{location}{name}')):
        mkdir(convert_url(f'{location}{name}'), 0o777)
