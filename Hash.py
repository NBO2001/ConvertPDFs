import hashlib
import mmap
from os import (walk)

def createHash(filename):

    h  = hashlib.sha1()

    with open(filename, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) as mm:
            h.update(mm)
    return h.hexdigest()



for path, subpath, files in walk("./safe/"):
    
    for file in files:  
        if path == "./safe/":
            extension = file.split(".")[len(file.split("."))-1]
        
            fileName = "".join(file.split(".")[:-1])
            
            if extension.upper() == "PDF":
                print(f'{file} : {createHash(f"./safe/{file}")}')

