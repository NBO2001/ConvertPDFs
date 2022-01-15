
import datetime
import sys
from os import (walk)
from PyPDF2 import (PdfFileReader, PdfFileWriter)
from time import time
from datetime import (date, datetime)


def create_arq_with_metadado(file, datas):

    olderArq = open(file, 'rb')
    olderDocument = PdfFileReader(olderArq)

    write_arq = PdfFileWriter()

    for page in range(olderDocument.getNumPages()):
        # Add pages in document
        write_arq.addPage(olderDocument.getPage(page))
    
    

    write_arq.addMetadata({
    '/Author': datas['Author'],
    '/Title': datas['Title'],
    '/Subject': datas['Subject'],
    '/Keywords': datas['keys'],
    '/Producer': 'NBOScripts - ConvertPDFs',
    '/Creator': 'https://github.com/NBO2001/ConvertPDFs',
    '/CreationDate': (datetime.now()).strftime("%Y%m%d%H%M%S")
    })

    name = f'{file.split(".")[0]} V2.pdf'
    newFile = open(name, 'wb')   

    write_arq.write(newFile)
    olderArq.close()

    newFile.close()





for path, subpath, files in walk("./"):

    for file in files:    
        extension = file.split(".")[len(file.split("."))-1]

        if extension.upper() == "PDF":

            create_arq_with_metadado(file, {
                "Author": "Natanael B",
                "Title": "WO 64984611",
                "Subject": "Work Order the Dezembro",
                "keys": "WO, 2021, Work Order, DEZEMBRO",
            })
            