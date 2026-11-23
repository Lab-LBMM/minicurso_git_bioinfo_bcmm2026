# Minicurso Git e Github para dados biológicos - BCMM 2026

## Organização do minicurso

O repositório é referente ao minicurso ministrado na data: 
Data: 22/10/2026
Horário: 14h às 18h

ministrantes e monitores:

 * Lorena Ferreira da Silva (monitor)
 * Julia Ferreira Santos (monitor)
 * Fabio Rodrigo de Freitas (monitor)
 * Stefany Renata Rodrigues (monitor)
 * Dr. Renato Augusto Corrêa dos Santos (ministrante)

## Resumo

Um dos princípios básicos da ciência é a reprodutibilidade. Em ciência de dados, define-se reprodutibilidade como a possibilidade de repetir os resultados a partir dos códigos e dados disponibilizados. Assim, o uso de ferramentas de controle de versão tornou-se essencial para garantir a organização, a rastreabilidade e a reprodutibilidade de projetos científicos. Na análise de dados biológicos, que frequentemente envolve múltiplos arquivos, scripts e colaboração entre pesquisadores, o Git e o GitHub permitem acompanhar alterações, recuperar versões anteriores e compartilhar projetos de forma eficiente. Neste minicurso, os participantes aprenderão os conceitos fundamentais de versionamento de códigos e as habilidades básicas de Git e GitHub por meio de atividades práticas utilizando sequências de genes. Serão abordados os principais comandos do Git, organização de repositórios, boas práticas de versionamento, colaboração em projetos e integração com o GitHub, sempre contextualizando sua aplicação em análises de sequências biológicas.

## Organização dos arquivos

O repositório está organizado em pastas para facilitar o acesso aos materiais utilizados nas atividades práticas do minicurso:

- **Dados:** arquivos de dados biológicos utilizados como entrada para as atividades de análise.
- **Problemas:** arquivos com os enunciados e desafios propostos aos participantes durante as atividades práticas.
- **Final:** arquivos com os resultados esperados ou soluções das atividades, permitindo comparar os resultados obtidos.

# Guia de criação de repositórios

Como material complementar, recomendamos a consulta ao guia elaborado por Lorena Ferreira da Silva, que apresenta orientações para a criação e organização de repositórios no GitHub.

# Instalação e dependências

O arquivo **requirements.txt** contém a lista de bibliotecas Python necessárias para executar os scripts do repositório. Ele facilita a instalação das dependências utilizadas nas atividades do minicurso.

Para instalar as bibliotecas, é necessário ter o Python instalado. Em seguida, execute no terminal, a partir da pasta principal do repositório:

```bash
pip install -r requirements.txt
```

# Como executar os scripts

Após clonar ou baixar o repositório, abra o terminal na pasta principal do projeto.

Os scripts das atividades práticas estão disponíveis na pasta *Problemas*.

**Problema 1 – Análise dos dados de RT-PCR**

Para executar o script utilize o comando:

```bash
python Problemas/Problema1.py
```

O script utiliza os dados disponíveis na pasta Dados/ e gera um gráfico de barras como resultado.

**Problema 2 – Busca de sequência de DNA**

Para executar o script:

```bash
python Problemas/Problema2.py
```

O script realiza a busca de uma sequência-alvo em uma sequência de DNA.

# Agradecimentos 

Agradecemos à Universidade Estadual Paulista (UNESP), ao Instituto de Biociências (IB), Câmpus de Rio Claro, e ao Programa de Pós-Graduação em Biologia Celular e Molecular (BCMM) pelo apoio institucional à realização deste minicurso.

Agradecemos também à Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP) pelo apoio à pesquisa e à formação científica.

