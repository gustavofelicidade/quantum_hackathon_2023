import pandas as pd
import numpy as np
import requests
import os

df = pd.read_csv("dataset/FUNDOS_E_DOCUMENTOS.csv", sep=";")

# print(df.head())
# print(df.columns)
# print(len(df['Administrador'].unique()))

unique_list = df['Administrador'].unique()
df_filtred = df.copy()

df_filtred = df_filtred.groupby('Administrador').apply(
    lambda df: df.iloc[0, :])

if not os.path.exists('data'):
    os.makedirs('data') 


for i in range(0, df_filtred.shape[0]):
    url = df_filtred.iloc[i]['Regulamento']
    adm = df_filtred.iloc[i]['Administrador']
    response = requests.get(url)
    with open(f'data/{adm}.pdf', 'wb') as f:
        f.write(response.content)
