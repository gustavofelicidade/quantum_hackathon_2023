import openai
from dotenv import load_dotenv
from extract_text import extract
import os

load_dotenv()

secret_key = os.getenv("SECRET_API")

openai.api_key = secret_key

def call_gpt(prompt):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[ {"role": "user", "content": prompt }],
    )

    return completions.choices[0].message.content


def run():
    keys = {"administração": [["taxa", "porcento"], ["taxa", "%"]],
    "social": [["fim", "exercício"]],
    "resgate": [["pagamento"],["cota"],["conversão"]]
    }

    pdfs_names = os.listdir("data")
    all_pdfs = []

    for i in range(5):
        respostas = {}
        respostas['pdf'] = pdfs_names[i]
        for key in keys:
            if key == 'administração':
                all_text = []
                for k in range(0, len(keys[key])):
                    all_text.append(extract(pdfs_names[i], key, keys[key][k]))
                prm = f'Responda com "Taxa de Administração: valor%", substituindo valor com o dado correto retirado desse texto: {all_text}'
                prm = prm.replace('[', '')
                prm = prm.replace(']', '')
                if len(prm) > 4090:
                    prm = prm[:4090]
                response = call_gpt(prm)
                respostas['Taxa de Administração'] = response          

            if key == 'social':
                all_text = []
                respostas['pdf'] = pdfs_names[i]
                for k in range(0, len(keys[key])):
                    all_text.append(extract(pdfs_names[i], key, keys[key][k]))
                prm = f'Responda com "Fim do exercício social: mes", substituindo mes com o dado correto retirado desse texto: {all_text}'
                prm = prm.replace('[', '')
                prm = prm.replace(']', '')
                if len(prm) > 4090:
                    prm = prm[:4090]
                response = call_gpt(prm)
                respostas['Fim do exercício social'] = response
            
            if key == 'resgate':
                all_text = []
                respostas['pdf'] = pdfs_names[i]
                for k in range(0, len(keys[key])):
                    all_text.append(extract(pdfs_names[i], key, keys[key][k]))
                prm = f'Responda com "Conversão da cota para resgate: valor", substituindo valor com o dado correto retirado desse texto: {all_text}'
                prm = prm.replace('[', '')
                prm = prm.replace(']', '')
                if len(prm) > 4090:
                    prm = prm[:4090]
                response = call_gpt(prm)
                respostas['Conversão da cota para resgate'] = response

        all_pdfs.append(respostas)

    print(all_pdfs)
    return all_pdfs


