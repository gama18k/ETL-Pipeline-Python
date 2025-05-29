# Projeto de ETL com Python

Este repositório contém um projeto simples de ETL (Extract, Transform, Load) implementado em Python, utilizando dados de duas empresas fictícias em formatos diferentes (JSON e CSV). O objetivo é consolidar essas informações em um único dataset padronizado.

## 📁 Estrutura do Projeto

├── data_raw/                # Dados brutos (input)
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/          # Dados transformados (output)
│   └── dados_combinados.csv
├── pipeline_versao_classemetodo.py  # Pipeline usando método de classe
├── pipeline_versao_instancia.py      # Pipeline usando instância direta
├── dados_modelo_classemetodo.py      # Classe Dados com @classmethod
└── dados_modelo_instancia.py          # Classe Dados com suporte a lista e leitura flexível



## ⚙️ Funcionalidades

- Leitura de arquivos JSON e CSV.
- Padronização de colunas entre diferentes fontes de dados.
- Junção dos dados em uma única estrutura unificada.
- Salvamento dos dados finais em formato `.csv`.

## 🧠 Lógica do ETL

### Extract
Os dados são lidos dos arquivos localizados em `data_raw/`, utilizando diferentes estratégias de leitura (métodos de classe ou instância).

### Transform
A padronização é feita com base em um mapeamento de colunas da empresa B para igualar o formato da empresa A.

### Load
Os dados consolidados são salvos em `data_processed/dados_combinados.csv`.

## 🐍 Requisitos

- Python 3.7+
- Nenhuma biblioteca externa é necessária (usa apenas `json` e `csv`).

## 📌 Observações

Duas implementações diferentes da classe `Dados` foram criadas:
- Uma com métodos estáticos e de classe.
- Outra com leitura direta via instância e suporte a dados em memória (`list`).

