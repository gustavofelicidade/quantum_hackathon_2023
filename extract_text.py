import PyPDF2

pdf_file = open('data/4UM Investimentos.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ''

for page_num in range(len(pdf_reader.pages)):
    page_obj = pdf_reader.pages[page_num]
    text += page_obj.extract_text()

pdf_file.close()

print(text)
print("Número de caracteres extraídos: ", len(text))