import json
import csv

# Classe para ler, manipular e salvar dados em diferentes formatos

class Dados:

    def __init__(self, path, tipo_dados):
    # Inicializa a classe com o caminho do arquivo e o tipo dos dados ('csv', 'json' ou 'list')
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()

    # Lê dados de um arquivo JSON
    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

     # Lê dados de um arquivo CSV

    def leitura_csv(self):

        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv
        # Decide qual método de leitura usar com base no tipo de dados

    def leitura_dados(self):
        dados = []

        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()
        
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()
            
        # Se os dados forem passados como uma lista de dicionários em memória

        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = "lista em memoria"

        return dados

        # Retorna o nome das colunas com base no último item da lista de dados

    def get_columns(self):
        return list(self.dados[-1].keys())
        # Renomeia as colunas conforme um dicionário de mapeamento passado (ex: {'old': 'new'})

    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
        # Retorna a quantidade de linhas de dados

    def size_data(self):
        return len(self.dados)


    # Junta os dados de duas instâncias da classe Dados
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list, 'list')

        # Converte os dados em uma tabela (lista de listas), onde a primeira linha são os nomes das colunas
        
    def transformando_dados_tabela(self):
        
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
            # Garante que mesmo colunas ausentes sejam representadas com 'Indisponivel'

                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela
    
    # Salva os dados transformados em formato de tabela como um novo arquivo CSV

    def salvando_dados(self, path):

        dados_combinados_tabela = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)