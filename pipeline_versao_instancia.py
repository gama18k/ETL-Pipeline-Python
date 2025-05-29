# Importa a classe Dados do módulo de processamento
from processamento_dados import Dados

# Define os caminhos dos arquivos de dados brutos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# ----------------------------
# ETAPA 1 - EXTRACT
# ----------------------------

# Cria uma instância de Dados para a empresa A, lendo um arquivo JSON

dados_empresaA = Dados(path_json, 'json')

# Exibe as colunas e o número de registros do arquivo da empresa A
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

# Cria uma instância de Dados para a empresa B, lendo um arquivo CSV
dados_empresaB = Dados(path_csv, 'csv')

# Exibe as colunas e o número de registros do arquivo da empresa B
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)


# ----------------------------
# ETAPA 2 - TRANSFORM
# ----------------------------

# Define o dicionário de mapeamento de nomes de colunas da empresa B 
# para padronizar com os nomes usados pela empresa A
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

# Renomeia as colunas da empresa B conforme o mapeamento definido
dados_empresaB.rename_columns(key_mapping)

# Exibe as colunas atualizadas da empresa B
print(dados_empresaB.nome_colunas)

# Junta os dados das duas empresas em uma nova instância
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

# Exibe as colunas e a nova quantidade total de registros combinados
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)


# ----------------------------
# ETAPA 3 - LOAD
# ----------------------------

# Define o caminho para salvar o arquivo com os dados combinados
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Salva os dados combinados em formato CSV
dados_fusao.salvando_dados(path_dados_combinados)

# Exibe o caminho do arquivo salvo como confirmação
print(path_dados_combinados)