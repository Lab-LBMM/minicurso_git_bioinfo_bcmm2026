##Código criado para o Minicurso de git e github##
##Autores:

#bibliotecas/pacotes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importação dos dados 
dados_IL1 = pd.read_csv("RT-PCR_IL1.csv", header=0)

#Calculo da média
media = dados_IL1.mean()
#print(media)
#print(dados_IL1)

#Organizando a tabela para criar o gráfico
dados_IL1_long = pd.melt(dados_IL1, var_name="Amostra", value_name="Resultado")
print(dados_IL1_long.head())
dados_IL1_long = dados_IL1_long.Amostra.str.split("_", expand=True)
print(dados_IL1_long)

#Organizando a tabela

#Gráfico
plt.bar(dados_IL1.columns, media, color = "blue", edgecolor = "black", linewidth = 2, hatch = '/')
plt.title("Quantificação de IL-1β por RT-PCR", fontsize = 18)
plt.ylabel("IL-1β/GAPDH", fontsize = 14)
plt.xlabel("Amostras", fontsize = 14)
plt.savefig("Gráfico_barras.png", dpi = 600, bbox_inches = "tight")
plt.show()



