import os
import PyPDF2
import PyPDF4
from PyPDF4 import PdfFileReader

import re
import docx_to_pdf

# Para cada PDF na pasta data
# Para cada PDF na pasta data
def read_pdfs(num_pdfs):
    folder_path = './data'
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')][:num_pdfs]

    for file_name in pdf_files:
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PdfFileReader(pdf_file)
                # pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ''
                for page_num in range(len(pdf_reader.pages)):
                    page_obj = pdf_reader.pages[page_num]
                    text += page_obj.extractText()
                pdf_file.close()

                parameters_count = {}
                parameters = ["Artigo", "numérico", "romanos"]

                for param in parameters:
                    count = 0
                    if param == "numérico":
                        count = len(re.findall(r'\b\d+\.\d+\b', text))
                    elif param == "romanos":
                        count = len(re.findall(r'\b[IVXLCDM]+\b', text))
                    else:
                        words = text.split()
                        for word in words:
                            if word == param:
                                count += 1
                    parameters_count[param] = count

                print(f"Results for {file_name}:")
                for param, count in parameters_count.items():
                    print(f"{param}: {count}")
        except PyPDF4.utils.PdfReadError:
            print(f"Error reading {file_name}. Skipping...")
            continue

    return None


if __name__ == '__main__':
    print(read_pdfs(62))