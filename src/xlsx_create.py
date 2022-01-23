from openpyxl import Workbook
from src.utils import (scan_in_folder, verify_file)

def new_xml():
    wb = Workbook()

    ws = wb.active
    ws.title = "Elements"
    ws.append(["Nome do arquivo", "Título", "Assunto", "Palavras chaves"])

    for file in scan_in_folder('./'):
        
        is_true, fileName, extension = verify_file(file, "pdf")
        
        if is_true:
            ws.append([file])


    return wb.save("list.xlsx")
