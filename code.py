##Código criado para o Minicurso de git e github##
##Autores:

#bibliotecas/pacotes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importação dos dados 
dados = pd.read_csv("RT-PCR_IL1.csv")

#Calculo da média
media = dados.mean()
print(media)

print(dados)


#Organizando a tabela
#ados_long = 


#Gráfico
plt.bar(dados.columns, media, color = "blue", edgecolor = "black", linewidth = 2, hatch = '/')
plt.title("Quantificação de IL-1β por RT-PCR", fontsize = 18)
plt.ylabel("IL-1β/GAPDH", fontsize = 14)
plt.xlabel("Amostras", fontsize = 14)
plt.savefig("Gráfico_barras.png", dpi = 600, bbox_inches = "tight")
plt.show()



