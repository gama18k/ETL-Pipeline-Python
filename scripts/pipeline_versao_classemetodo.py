# Importa a classe Dados de um módulo chamado processamento_dados_desafio
from processamento_dados_desafio import Dados

# Define os caminhos dos arquivos de entrada (dados brutos)
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


# ----------------------------
# ETAPA 1 - EXTRACT
# ----------------------------

# Lê os dados da empresa A a partir de um arquivo JSON usando o método de classe
dados_empresaA = Dados.leitura_dados(path_json, 'json')

# Exibe as colunas e o número de registros da empresa A
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

# Lê os dados da empresa B a partir de um arquivo CSV
dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
# Exibe as colunas e o número de registros da empresa B
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)


# ----------------------------
# ETAPA 2 - TRANSFORM
# ----------------------------

# Define o mapeamento de nomes de colunas para padronizar os dados da empresa B
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

# Renomeia as colunas da empresa B de acordo com o mapeamento
dados_empresaB.rename_columns(key_mapping)

# Exibe as colunas atualizadas após a padronização
print(dados_empresaB.nome_colunas)

# Junta os dados da empresa A e empresa B em uma nova instância da classe Dados
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
# Exibe as colunas e o número total de registros combinados
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)


# ----------------------------
# ETAPA 3 - LOAD
# ----------------------------

# Define o caminho do arquivo de saída com os dados combinados
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Salva os dados combinados no caminho especificado em formato CSV
dados_fusao.salvando_dados(path_dados_combinados)

# Exibe o caminho do arquivo salvo como confirmação
print(path_dados_combinados)
