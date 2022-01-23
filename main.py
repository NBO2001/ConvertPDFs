try:
    from sys import argv
    
    from PyPDF2 import (PdfFileReader)

    from src.xlsx_create import ( new_xml )

    from src.xlsx_read import ( readfile )

    from src.metadadosadd import MetadadosAdd

    from src.converterpdf import ConverterPDF

    from src.utils import (
        file_is_exists, 
        create_folder, 
        folder_is_exists, 
        file_remove,
        folder_remove,
        convert_url)
    
except Exception as e:
    print(e)


class App:
    def __init__(self, author: str) -> None:

        self.author = author

        if (
            not file_is_exists('list.xlsx') 
            or not folder_is_exists(convert_url("./proc")) 
            or not folder_is_exists(convert_url("./safe"))
            ) :

            new_xml()
            create_folder("proc")
            create_folder("safe")
        else:
            self.start()

    def for_pdf_a(self, file: str):

        conv = ConverterPDF(f'./proc/{file}',f'./safe/{file}')
        conv.converter()

    def start(self):

        files = readfile()

        for file in files:

            file_name, title, subject, keywd = file

            olderArq = open(file_name, 'rb')

            olderDocument = PdfFileReader(olderArq)

            meta = MetadadosAdd(olderDocument, {
                "Author":self.author,
                "Title": title,
                "Subject": subject,
                "keys": keywd,
                "location": "Manaus - AM"
            })
            meta.create_file(f'./proc/{file_name}')
            olderArq.close()

            file_remove(f'./{file_name}')

            self.for_pdf_a(file_name)

            file_remove(f'./proc/{file_name}')


        file_remove('./list.xlsx')    
        folder_remove(f'./proc')
    


if __name__ == "__main__":
    try:
        
        if len(argv) <= 1:
            raise TypeError(f'Its necessary to inform the author')
        
        App(argv[1])

    except Exception as error:

        print(error)