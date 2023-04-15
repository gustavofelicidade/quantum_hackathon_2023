# O projeto: Criar e disponibilizar um código
# capaz de retornar dados estruturados de fundos de
# investimento a partir dos regulamentos dos fundos.


# importar bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import reportlab
import logging

# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
log = logger.info


# Ler dados

agrupado_administradoras = r'C:\Users\123\PycharmProjects\quantum\dataset\AGRUPADO_ADMINISTRADORAS.csv'
fundos_e_documentos = r'C:\Users\123\PycharmProjects\quantum\dataset\FUNDOS_E_DOCUMENTOS.csv'


# Leitura de dados
dados1 = pd.read_csv(agrupado_administradoras)
fundos = pd.read_csv(fundos_e_documentos)


# Explorar dados
log(dados1.head)
log(fundos)
# log(fundos.head)




# Extração de dados




#  Taxa de administração (porcentagem);
#  Taxa de administração (financeira);
#  Conversão da cota para resgate;
#  Disponibilização dos recursos para resgate;
#  Fim do exercício social