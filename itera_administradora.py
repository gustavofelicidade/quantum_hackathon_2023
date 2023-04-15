import os
from PyPDF4 import PdfFileReader

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
            #  Adicionar Funções do extract_text.py
            #===================================================================
            text = ''
            for page_num in range(pdf_reader.getNumPages()):
                page_obj = pdf_reader.getPage(page_num)
                text += page_obj.extractText()


            print(text)
            # extrair o texto de todas as páginas do PDF e imprimir na tela
            pdf_file.close()
            #===================================================================


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