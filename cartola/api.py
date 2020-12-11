import requests
import json
import os


class ApiClient(object):
    """Um cliente para a API do Cartola FC.

    Args:
       url(str): URL com um endpoint da API do cartola.
       data(object): Dados da API no formato json.
    """

    def __init__(self, url=""):
        self.url = url
        self.data = requests.get(url).json()

    def get_json(self):
        """Obtém os dados no formato json.
        Returns:
        ----------
        Retorna um objeto json.
        """
        return self.data

    def get_data_by_key(self, key):
        """Busca dados no objeto json.
        Args:
        ----------
        key(str): Chave atrelada aos dados.

        Returns:
        ----------
        Retorna os dados associados a uma key.
        Se a key não existir, é retornado None.
        """

        if key in self.data:
            return self.data[key]

        return None

    def save_as_json(self, dir_path, round):
        """Salva os dados no formato json.
        Args:
        ----------
        dir_path(str): Caminho do diretório.
        round(str): Número da rodada.
        """
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        api_name = self.url.split('.com/')[-1].replace('/', '_')
        file_name = fr'/{api_name}_{str(round)}.json'
        path = dir_path + file_name

        try:
            with open(path, 'w', encoding='utf-8') as fp:
                json.dump(self.data, fp, ensure_ascii=False)

        except IOError:
            print("I/O error")
