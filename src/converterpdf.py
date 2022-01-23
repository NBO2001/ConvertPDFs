from locale import getpreferredencoding
from ghostscript import Ghostscript


class ConverterPDF:
    def __init__(self,file_input, file_output):
        self.args = [
                "ps2pdf",
                "-dPDFA","-dNOPAUSE", "-dBATCH", "-dSAFER","-dUseCIEColor", "-sProcessColorModel=DeviceCMYK",
                "-sDEVICE=pdfwrite","-sPDFACompatibilityPolicy=1",
                f'-sOutputFile={file_output}',
                "-c", ".setpdfwrite",
                "-f",  f'{file_input}'
                ]

        self.encoding = getpreferredencoding()

    def converter(self):
        
            args = [a.encode(self.encoding) for a in self.args]

            Ghostscript(*args)