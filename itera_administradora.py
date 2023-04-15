import os
from PyPDF4 import PdfFileReader
import docx_to_pdf
# Para cada PDF na pasta data
def read_pdfs(num_pdfs):
    folder_path = './data'

    # Leia se for PDF
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')][:num_pdfs]


    #  Se não for PDF converta para PDF:

    for file_name in pdf_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)


            #===================================================================
            #  Aplicar tratamento de acordo com o caso
            #===================================================================

            parameter = ["Artigos", "Numérico", "Romanos"]

            match parameter:

                case "Artigos":
                    # do_something(first)
                    ...

                case "Numérico":
                    # do_something(second)
                    ...

                case "Romanos":
                    # do_something(third)
                    ...



if __name__ == '__main__':
    read_pdfs(2)