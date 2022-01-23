from PyPDF2 import (PdfFileWriter)
from datetime import (datetime)


class MetadadosAdd:
    def __init__(self, olderDocument, datas):
        self.datas = datas
        
        self.validate_datas()
        
        self.document = olderDocument
        

    def create_file(self, save_in):
        self.write_arq = PdfFileWriter()

        for page in range(self.document.getNumPages()):
            # Add pages in document
            self.write_arq.addPage(self.document.getPage(page))

        self.insert_metadata()

        newFile = open(save_in, 'wb')   

        self.write_arq.write(newFile)

        newFile.close()


    def validate_datas(self):
        if self.datas:
            if ( not self.datas['Author'] 
            or not self.datas['Title']
            or not self.datas['Subject'] 
            or not self.datas['keys'] 
            or not self.datas['location']):
                raise TypeError(f'Required data not found')

    def insert_metadata(self):

        self.write_arq.addMetadata({
        '/Author': self.datas['Author'],
        '/Title': self.datas['Title'],
        '/Subject': self.datas['Subject'],
        '/Keywords': self.datas['keys'],
        '/Local': self.datas['location'],
        '/Producer': 'NBOScripts - ConvertPDFs',
        '/Creator': 'https://github.com/NBO2001/ConvertPDFs',
        '/CreationDate': (datetime.now()).strftime("%Y%m%d%H%M%S")
        })


