# Importa as bibliotecas
from extract_text import *
import pandas as pd
import run_openai
# import json

# # Pega os dados a partir de extract_text
# string_de_dados = ''

# # Converte dados recebidos para json
# dict_dados = json.load(string_de_dados)

def convert2csv(dados):
    # Cria um dataframe a partir do dicionário
    df = pd.DataFrame(dados)
    # Cria um csv a partir do dataframe
    print("Criando csv...")
    df.to_csv("solucao_desafio.csv", index=None, header=True, sep=';')

convert2csv(run_openai.run())
