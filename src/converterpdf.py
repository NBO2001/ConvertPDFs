from locale import getpreferredencoding
from ghostscript import Ghostscript


class ConverterPDF:
    def __init__(self,file_input: str, file_output: str) -> None:
        self.args = [
                "ps2pdf",
                "-dPDFA","-dNOPAUSE", "-dBATCH", "-dSAFER", "-sProcessColorModel=DeviceCMYK",
                "-sDEVICE=pdfwrite","-sPDFACompatibilityPolicy=1",
                f'-sOutputFile={file_output}',
                "-c", ".setpdfwrite",
                "-f",  f'{file_input}'
                ]

        self.encoding = getpreferredencoding()

    def converter(self):
        
            args = [a.encode(self.encoding) for a in self.args]

            Ghostscript(*args)