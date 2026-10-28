# Guia Prático de Git e GitHub para Pesquisadores

Versionar o código, os dados e os textos da sua pesquisa é essencial para garantir a reprodutibilidade científica, evitar a perda de arquivos e facilitar a colaboração com seu orientador e colegas de laboratório.

---

## 1. Conceitos Básicos: Git vs. GitHub

Antes de colocar a mão na massa, vale a pena relembrar a diferença entre as duas ferramentas:

* **Git:** É o sistema de controle de versão instalado no seu computador. Ele registra cada alteração feita nos arquivos, permitindo que você volte no tempo se algo der errado.
* **GitHub:** É a plataforma online (nuvem) onde você hospeda seus repositórios Git, facilitando o backup, o compartilhamento e a visualização do seu trabalho.

---

## 2. O Que Deve (e o Que Não Deve) Constar no Repositório

Organizar bem o seu repositório garante que qualquer pessoa (ou você mesmo daqui a algum tempo) consiga entender e reproduzir o seu estudo.

### O que incluir:
* **Scripts e códigos de análise:** Códigos em Python, R, Julia, Bash, etc.
* **Documentação clara (`README.md`):** Um guia explicativo sobre o projeto.
* **Estrutura de pastas padronizada:** Separando dados brutos, processados e resultados.
* **Arquivos de dependências:** Listas de bibliotecas e pacotes necessários (ex: `requirements.txt` ou `environment.yml`).

### O que NUNCA incluir:
* **Dados brutos pesados:** Arquivos gigantescos (gigabytes de imagens, leituras brutas de sequenciamento, etc.) não devem ir para o GitHub. Use repositórios de dados dedicados (como Zenodo, Figshare ou Dryad) e coloque apenas o link no seu projeto.
* **Chaves de API, senhas ou tokens:** Credenciais nunca devem ser expostas publicamente.
* **Arquivos temporários do sistema:** Como arquivos `.DS_Store` (Mac) ou `thumbs.db` (Windows).

---

## 3. Organização de Pastas Recomendada

Uma estrutura limpa e intuitiva economiza tempo e demonstra rigor científico. Veja um modelo padrão recomendado para projetos de pesquisa:

```text
meu-projeto-pesquisa/
├── README.md             # Descrição geral do projeto, objetivos e como rodá-lo
├── LICENSE               # Licença de uso do código/pesquisa
├── .gitignore            # Lista de arquivos que o Git deve ignorar
│
├── data/                 # (Opcional/Pequeno) Dados processados ou amostras
│   ├── raw/              # Dados brutos (geralmente ignorados pelo Git se forem grandes)
│   └── processed/        # Dados limpos prontos para análise
│
├── scripts/              # Códigos de análise, limpeza e modelagem
│   ├── 01_limpeza.py
│   └── 02_analise_estatistica.R
│
├── outputs/              # Resultados gerados (gráficos, tabelas, relatórios)
│   ├── figures/
│   └── tables/
│
└── docs/                 # Documentação adicional
```

---

## 4. Passo a Passo: Criando seu Primeiro Repositório

### Passo 1: Instalação e Configuração Inicial
Se ainda não tiver o Git instalado, baixe-o em [git-scm.com](https://git-scm.com). Abra o terminal (ou Prompt de Comando) e configure seu nome e e-mail (os mesmos usados no GitHub):

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu.email@gmail.br"
```

### Passo 2: Criar o Repositório no GitHub
1. Acesse [github.com](https://github.com) e faça login.
2. No canto superior direito, clique no ícone **+** e selecione **New repository** (Novo repositório).
3. **Repository name:** Dê um nome claro e sem espaços (ex: `analise-ecologica-formigas`).
4. **Description:** Escreva uma breve descrição do que se trata o projeto.
5. Escolha se será **Public** (visível para todos, ideal para ciência aberta) ou **Private** (visível apenas para você e colaboradores convidados).
6. **Importante:** Marque a opção **Add a README file** (Adicionar um arquivo README).
7. Em **Add .gitignore**, escolha a linguagem principal do seu projeto (ex: Python ou R). Isso evita que arquivos indesejados sejam enviados por engano.
8. Clique em **Create repository**.

### Passo 3: Clonar o Repositório para o seu Computador
No repositório que você acabou de criar no GitHub:
1. Clique no botão verde **Code**.
2. Copie a URL HTTPS.
3. Abra o terminal no seu computador na pasta onde deseja guardar o projeto e digite:

```bash
git clone <cole-a-url-aqui>
cd nome-do-repositorio
```

Agora você tem uma cópia local conectada ao GitHub.

---

## 5. O Ciclo de Trabalho Diário (Boas Práticas de Versionamento)

Para registrar o progresso da sua pesquisa, você usará um ciclo simples de três etapas no terminal:

1. **Verifique o status:** Veja quais arquivos foram modificados.
   ```bash
   git status
   ```
2. **Adicione as alterações:** Prepare os arquivos que deseja salvar (*o ponto adiciona todas as modificações da pasta atual*).
   ```bash
   git add .
   ```
3. **Crie um ponto de salvamento (Commit):** Salve as alterações com uma mensagem descritiva explicando o que você mudou e por quê.
   ```bash
   git commit -m "Adiciona script de limpeza de dados e atualiza gráfico de abundância"
   ```
4. **Envie para o GitHub (Push):** Sincronize suas alterações locais com a nuvem.
   ```bash
   git push
   ```

---

## 6. Dicas de Ouro para Pesquisadores

* **Mensagens de commit claras:** Evite mensagens genéricas como "arrumando o código" ou "teste". Prefira algo informativo como *"Corrige cálculo de desvio padrão na linha 45"* ou *"Adiciona novas variáveis climáticas ao modelo"*.
* **Faça commits frequentes:** Não espere terminar o projeto inteiro para salvar. Faça commits sempre que concluir uma etapa lógica (ex: um gráfico pronto, um teste estatístico validado).
* **O arquivo `README.md` é seu cartão de visitas:** Escreva de forma simples o título da pesquisa, o objetivo, o autor, os requisitos de software e um passo a passo rápido de como rodar os scripts. Isso garante a reprodutibilidade do seu estudo.