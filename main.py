try:

    from tkinter import Tk
    from os import (walk)
    from PyPDF2 import (PdfFileReader, PdfFileWriter)
    from time import time
    from datetime import (date, datetime)
    from src.xlsx_create import ( new_xml )
    from src.xlsx_read import ( readfile )
    from src.metadadosadd import MetadadosAdd
    from src.converterpdf import ConverterPDF
    from src.utils import (
        file_is_exists, 
        create_folder, 
        folder_is_exists, 
        file_remove,
        folder_remove)
    
except Exception as e:
    print(e)


def for_pdf_a(file):

    conv = ConverterPDF(f'./proc/{file}',f'./safe/{file}')
    conv.converter()



if not file_is_exists('list.xlsx') or not folder_is_exists("./proc") or not folder_is_exists("./safe") :
    new_xml()
    create_folder("proc")
    create_folder("safe")
else:

    files = readfile()

    for file in files:

        file_name, title, subject, keywd = file

        olderArq = open(file_name, 'rb')

        olderDocument = PdfFileReader(olderArq)
   
        meta = MetadadosAdd(olderDocument, {
            "Author": "Natanael B",
            "Title": title,
            "Subject": subject,
            "keys": keywd,
            "location": "Manaus - AM"
        })
        meta.create_file(f'./proc/{file_name}')
        olderArq.close()

        file_remove(f'./{file_name}')

        for_pdf_a(file_name)
        
        file_remove(f'./proc/{file_name}')


    file_remove('./list.xlsx')    
    folder_remove(f'./proc')

    