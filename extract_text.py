import PyPDF2

pdf_file = open('data/4UM Investimentos.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ''

for page_num in range(len(pdf_reader.pages)):
    page_obj = pdf_reader.pages[page_num]
    text += page_obj.extract_text()

pdf_file.close()


print(sorted(list(set(text))))
text = text.replace('-', '')
text = text.replace('_', '')
text = text.replace('“', '')
text = text.replace('”', '')
text = text.replace('@', '')
text = text.replace('(', '')
text = text.replace(')', '')

#print(text[12000:14000].replace('\n', ''))
print("Número de caracteres extraídos: ", len(text))

words = ["administração", "social", "cota", "%", "taxa"]
window_size = 10

extracted_text = []

for word in words:
    start_index = 0
    while True:
        start_index = text.find(word, start_index)
        if start_index == -1:
            break
        context_start = max(0, start_index - window_size)
        context_end = min(len(text), start_index + len(word) + window_size)
        extracted_text.append(text[context_start:context_end])
        start_index += 1

print(extracted_text)

