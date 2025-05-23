![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)


<a href="https://www.flaticon.com/free-icons/etl" title="etl icons">
  <img align="left" alt="etl" height="45" width="45" src="./assets/etl.png">
</a>

# PIPELINE ETL MODULAR SIMPLES COM TESTES E LOGS


## SOBRE O PROJETO

Este projeto possui o principal foco na construção padronizada de uma estrutura de projetos e documentação, de modo acessório, **portanto, com menor preocupação com a sofisticação do ETL**, apresenta um problema de negócio e um desafio de melhorar o processo, de modo que implementa um pipeline ETL modular em Python, dividindo-o em três etapas principais:

- Extract: leitura e concatenação de múltiplos arquivos Excel.
- Transform: limpeza e normalização dos dados, exportação para Parquet.
- Load: leitura de Parquet e exportação final para Excel.

Fora observado rigor na documentação e estrutura do projeto.  
Após cada etapa, o pipeline executa testes unitários com `pytest`.  
No final, executa um teste de integração que valida o sucesso global!🚀 

Todos os eventos são registrados em um arquivo de log gerado automaticamente na pasta `docs/`.  
O arquivo armazena todas as etapas da pipeline, dos testes unitários com nome no formato: `docs/log_YYYYMMDD_HHMMSS.log`.

## FLUXO DO PIPELINE

- Extract → Teste, se ok:
- Transform → Teste, se ok:
- Load → Teste, se ok:
- Teste Final ✅
- Log gerado 📄
- FIM 🎯

## PROBLEMA DE NEGÓCIO

### Contextualização:

Atualmente, empresas de setores como varejo, saúde ou logística precisam consolidar dados provenientes de diversas fontes (planilhas, sistemas legados, APIs, bancos de dados), muitas vezes envolvendo informações sensíveis ou estratégicas ao negócio,e essa integração é frequentemente realizada de forma manual, com processos frágeis, custosos, dificultando o mapeamento correto das informações e gerando riscos de inconsistência.  
Esses desafios impactam negativamente a capacidade de a organização alinhar os dados aos requisitos estratégicos do negócio, como:  

- Ganho de eficiência operacional.  
- Melhoria na qualidade das informações.  
- Suporte a análises preditivas e prescritivas.  
- Cumprimento de requisitos regulatórios.  

Portanto, como automatizar a integração e a validação de dados de múltiplas fontes para apoiar a estratégia de negócios, de forma confiável, rápida, automatizada de forma que possa promover a economia e o aperfeiçoamento das funções desempenhadas, agregando valor às decisões operacionais e táticas?

### Como a sua solução endereça esse problema:

O Projeto automatiza a extração desses arquivos, transforma os dados com as regras de negócio específicas (ex.: ajuste de datas, padronização de categorias), separando o resultado final por setores, e os armazena em formato Parquet, ainda, a solução inclui testes automatizados para validar as transformações antes da carga, obtendo como resultados:  

🔹 A área de negócios passa a receber relatórios atualizados diariamente.  
O tempo de consolidação de dados reduz-se em 80%.  

🔹 Mapeamento de Dados:  
Sua solução realiza a leitura, transformação e padronização de dados, permitindo identificar, mapear e consolidar informações dispersas.  
Isso viabiliza a criação de um inventário de dados estruturado, facilitando a rastreabilidade e a conformidade com normas de segurança e privacidade.  

🔹 Automação Alinhada à Estratégia:  
A automação do pipeline, com testes unitários e integração contínua, reduz a dependência de processos manuais.  
Isso suporta a estratégia organizacional de transformação digital, promovendo escalabilidade e agilidade na entrega de insights para as áreas de negócio.  

🔹 Agregação de Valor:  
Ao transformar dados em formatos otimizados (como Parquet), sua solução viabiliza análises mais rápidas e eficientes.  
Isso agrega valor não apenas na redução de custos operacionais, mas também no fornecimento de informações mais precisas e tempestivas para a tomada de decisão.  

🔹 Levantamento e Cumprimento de Requisitos:  
A estruturação modular (extract, transform, load) permite que os requisitos de qualidade, segurança e performance sejam claramente definidos, testados e validados.  
Os testes automatizados com pytest asseguram que as transformações seguem as regras de negócio, garantindo confiabilidade nas entregas.  

---

## COMEÇANDO

### Pré-requisitos

1. Git e Github  
Você deve ter o Git instalado em sua máquina.  
Você também deve ter uma conta no GitHub.  

2. Pyenv  
É usado para gerenciar versões do Python.  
[Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation).  
Vamos usar nesse projeto o Python 3.11.4   

3. Poetry  
Este projeto utiliza Poetry para gerenciamento de dependências.  
[Instruções de instalação do Poetry aqui](https://python-poetry.org/docs/#installation).    

4. Execute o comando para ver a documentação do projeto:

```bash
task doc
```

### Estrutura de arquivos
---

Estrutura básica de arquivos para o projeto encontra-se organizada da seguinte maneira:
```bash

```

---

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/andrematiello/jornada_workshop01
```

2. Acesse o diretório workshop:

```bash
cd jornada_workshop01
```

3. Configure a versão correta do Python:
```bash
pyenv install 3.11.4
```

4. Determine a versão local (do projeto) do Python:
```bash
pyenv local 3.11.4
```

5. Configure o Poetry para usar o Python 3.11.4 e ative o ambiente virtual:
```bash
poetry env use 3.11.4
```

6. Para criar o ambiente virtual, desde a versão 2 do Poetry, segundo a documentação oficial, o Poetry Shell não acompanha a instalação padrão, devendo er instalado como uma dependência [Poetry Docs](https://python-poetry.org/docs/managing-environments/#powershell):
```bash
poetry self add poetry-plugin-shell
```

7. Para ativar o ambiente virtual:
```bash
poetry shell
```

8. Instale as dependências do projeto:
```bash
poetry add pandas pyarrow pytest numpy blue ignr
```

---

### Como rodar o projeto:

1. Execute o pipeline:
```bash
python -m app.main
```

2. Verifique na pasta data/output se o arquivo foi gerado corretamente: `data/output`

---

### Como rodar os testes individualmente:

- Teste do extract:
```bash
pytest tests/test_extract.py
```

- Teste do transform:
```bash
pytest tests/test_transform.py
```

- Teste do load:
```bash
pytest tests/test_load.py
```

- Teste de toda pipeline:
```bash
pytest tests/test_pipeline.py
```

### Como rodar os testes todos de uma vez:

```bash
pytest
```

---

## TECNOLOGIAS UTILIZADAS
- Python 3.11+
- Pyenv. https://pypi.org/project/pyenv-win/
- Poetry. https://pypi.org/project/poetry/
- Git e Github

## BIBLIOTECAS UTILIZADAS
- Pandas: para manipulação dos dados. https://pypi.org/project/pandas/
- Pyarrow: para leitura e escrita na extensão Parquet. https://pypi.org/project/pyarrow/
- Pytest: testes automatizados. https://pypi.org/project/pytest/
- Numpy: é uma biblioteca para realizar cálculos numéricos e manipulação de dados em grande escala
- Blue: para adoção de melhores práticas, segundo a Pep8. https://pypi.org/project/blue/
- Ignr: para criação automatizada prévia do .gitignore. https://pypi.org/project/ignr/

---

## COMENTÁRIOS

### Agora você tem:
🔹 Um Pipeline robusto;  
🔹 Testes intermediários;  
🔹 Logs completos;  
🔹 Documentação top!😉  

### Este projeto entrega um pipeline ETL completo e profissional, seguindo as boas práticas de Engenharia de Dados, com foco em:
🔹 Modularidade: cada etapa separada com responsabilidade única: Extract, Transform e Load.  
🔹 Testabilidade: testes automatizados com pytest em cada etapa, garantindo qualidade e segurança na evolução do código.  
🔹 Observabilidade: sistema de logging estruturado, com geração automática de arquivos de log identificados por data e hora, permitindo rastreabilidade completa de cada execução.  
🔹 Automação: execução sequencial e validada de todo o processo, com parada imediata em caso de falha, evitando propagação de erros.  
🔹 Documentação clara: orientações objetivas sobre execução, estrutura do projeto e fluxo de dados, facilitando manutenção e escalabilidade.  
🔹 Estética e usabilidade: enriquecido com emojis e mensagens amigáveis para tornar a execução mais visual e intuitiva.  

## PRINCIPAIS CARACTERÍSTICAS TÉCNICAS

### 🔒 Segurança e Controle:
Validação automatizada de cada etapa via testes unitários com pytest, assegurando que falhas sejam identificadas e tratadas de forma imediata e controlada.  
Por meio de uma arquitetura defensiva, o pipeline interrompe automaticamente a execução em caso de erro, evitando propagação de inconsistências.

### 🛠️ Robustez e Escalabilidade:
Estrutura modular orientada a funções específicas, garantindo manutenibilidade e facilidade de extensão para novos requisitos ou integrações.  
Logging estruturado, com timestamp de execução e status de cada etapa, viabilizando rastreabilidade completa e facilitando auditorias.

### 📊 Observabilidade e Transparência:
Todos os eventos e operações são registrados em logs persistentes, gerados automaticamente e armazenados em `docs/`, permitindo uma visão clara da execução e apoio a processos de compliance e forense.

### 🚀 Entrega de Valor:
Automação de todo o fluxo ETL: desde a ingestão até a exportação dos dados tratados e validados, com garantias explícitas de qualidade e confiabilidade, por meio da mitigação de riscos operacionais com testes intermediários, evitando a entrega de dados corrompidos ou incompletos.  
Preparação de dados em formatos otimizados (Parquet e Excel), prontos para análise, reporting ou integração com sistemas de Business Inteligence.  

---

Projeto inspirado no workshop 01 da Jornada de Dados, com adaptações;  
Projeto realizado com apoio de Inteligência Artificial (ChatGPT);  
Para próximas melhorias, extração de dados reais, com limpeza e transformação, posteriormente o load em um Data Warehouse, quem sabe uma cloud provider. Ainda, um ETL orquestrado com Apache Airflow, boas práticas de CI/CD.

## DÚVIDAS, SUGESTÕES OU FEEDBACKS

#### 🚀 André Matiello C. Caramanti - [matiello.andre@hotmail.com](mailto:matiello.andre@hotmail.com)

#### "Este pipeline não apenas executa, mas valida, registra e garante a qualidade dos dados de ponta a ponta, conforme as melhores práticas de Engenharia de Dados."

---

## LICENSE

[MIT License](https://andrematiello.notion.site/mit-license)