import PyPDF2
import re


pdf_file = open('data/4UM Investimentos.pdf', 'rb')
#pdf_file = open('data/Ativa Investimentos.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ''

for page_num in range(len(pdf_reader.pages)):
    page_obj = pdf_reader.pages[page_num]
    text += page_obj.extract_text()

pdf_file.close()


#print(sorted(list(set(text))))
text = text.lower()
text = text.replace('-', '')
text = text.replace('_', '')
text = text.replace('“', '')
text = text.replace('”', '')
text = text.replace('@', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('\n', '')
text = text.replace('º', '')

text_splitted = text.split('Artigo')
text_re = re.split(r'artigo \d+'  , text)

def words_context(text, words, window_size=5):
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

    return extracted_text


def get_contexts(text, keyword, word_list, window_size=5):
    """
    This function takes a text string, a keyword string, a list of words, and a window size, and returns a list of
    context strings that contain the keyword string and at least one of the words in the list. The window size
    determines how many words before and after the keyword should be included in the context.
    """
    # Split the text into words and create an index of the keyword's positions
    words = text.split()
    keyword_positions = [i for i, word in enumerate(words) if word == keyword]
    
    # For each occurrence of the keyword, extract the surrounding context and check if any of the words are present
    contexts = []
    for pos in keyword_positions:
        start = max(0, pos - window_size)
        end = min(len(words), pos + window_size + 1)
        context = ' '.join(words[start:end])
        if all([word in context for word in word_list]):
            contexts.append(context)
    
    return contexts

#extracted_text = get_contexts('adminitração', text, 10)
#print(extracted_text)

extracted_context = words_context(text, ['administração'], 50)
#print(extracted_context)

for ctx in extracted_context:
    res = (get_contexts(ctx, 'administração', ['taxa', '%'], 20))
    if len(res) > 0:
        print(res)



