import json
import csv

class Dados:

    def __init__(self, dados):
        """
        Inicializa a instância com dados carregados (lista de dicionários).
        """
        self.dados = dados
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()


    def __leitura_json(path):
        """
        Método estático privado para ler dados de um arquivo JSON.
        """
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(path):
        """
        Método estático privado para ler dados de um arquivo CSV como dicionários.
        """
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []
        """
        Método de classe que cria uma instância de `Dados` lendo de um arquivo CSV ou JSON.
        """
        if tipo_dados == 'csv':
            dados = cls.__leitura_csv(path)
        
        elif tipo_dados == 'json':
            dados = cls.__leitura_json(path)

        return cls(dados)

        """
        Obtém os nomes das colunas com base no último dicionário da lista.
        """
    def __get_columns(self):
        return list(self.dados[-1].keys())

        """
        Renomeia as colunas dos dados com base em um dicionário de mapeamento.
        """
    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()

        """
        Conta quantas linhas existem nos dados.
        """
    def __size_data(self):
        return len(self.dados)

        """
        Junta duas instâncias de `Dados` em uma nova.
        """
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list)

        
    def __transformando_dados_tabela(self):
        
        """
        Converte os dados em formato de tabela (lista de listas) com cabeçalho.
        """
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela

    def salvando_dados(self, path):
        """
        Salva os dados atuais em um arquivo CSV, mantendo a estrutura tabular.
        """
        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)