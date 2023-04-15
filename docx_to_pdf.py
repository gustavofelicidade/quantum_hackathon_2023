from docx2pdf import convert

def convert_docx_to_pdf(docx_file_path, pdf_file_path):
    try:
        convert(docx_file_path, pdf_file_path)
        print("Conversão concluída com sucesso!")
    except Exception as e:
        print("Ocorreu um erro durante a conversão: ", e)
