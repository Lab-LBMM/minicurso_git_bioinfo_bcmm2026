##Código criado para o Minicurso de git e github##
##Autores:

#bibliotecas/pacotes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importação dos dados 
dados_IL1 = pd.read_csv("Dados/RT-PCR_IL1.csv", header=0)

#Organizando a tabela para criar o gráfico
dados_IL1_long = pd.melt(dados_IL1, var_name="Amostra", value_name="Resultado")
print(dados_IL1_long)
dados_IL1_long[['Genótipo', 'Condição']] = dados_IL1_long['Amostra'].str.split("_", expand=True)
#Calculo da média
tabela_medias = dados_IL1_long.groupby(['Genótipo', 'Condição'])['Resultado'].mean().unstack()
print(tabela_medias)

#Gráfico
plt.style.use('classic')
tabela_medias.plot(kind='bar',color=["darkred", "darkorange"], edgecolor="black", linewidth=1, figsize=(8, 8))
plt.title("Titulo", fontsize = 18)
plt.ylabel("Titulo_y", fontsize = 14)
plt.xlabel("Titulo_x", fontsize = 14)
plt.savefig("Gráfico_barras.png", dpi = 600, bbox_inches = "tight")
plt.show()





