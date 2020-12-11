import json
import os


class Clubs(object):
    """Um classe que representa os dados dos clubes no Cartola.
    Args:
    ----------
    json_data(object): Dados dos clubes no formato json.

    Attributes:
    ----------
    json_data(object): Dados dos clubes no formato json.
    club_data(list): Dados filtrados dos clubes.
    """

    def __init__(self, json_data):
        self.json_data = json_data
        self.club_data = []

    def club_information(self, club_ids, target_data):
        """Obtém os dados pelas keys contidas no objeto json.
        Args:
        ----------
        club_ids (list): Id´s dos clubes que participam do Cartola.
        data_target (list): Lista de dados que serão retonados.
        """

        for id in club_ids:
            d = self.json_data[str(id)]
            aux_dic = {str(k): str(d[k]) for k in target_data}
            self.club_data.append(aux_dic)

    def save_as_json(self, path):
        """Salva as informações dos clubes no formato json.
        Args:
        ----------
        path(str): Caminho e nome do arquivo.
        """

        try:
            with open(path, 'w', encoding="utf-8") as fp:
                json.dump(self.club_data, fp, ensure_ascii=False)

        except IOError:
            print("I/O error")

    def save_as_csv(self, path):
        """Salva as informações dos clubes no formato csv.
        Args:
        ----------
        path(str): Caminho e nome do arquivo.
        """

        # Pega o nome das colunas.
        csv_columns = self.club_data[0].keys()

        try:
            with open(path, 'w', encoding="utf-8") as csv_file:
                csv_file.write(','.join(csv_columns) + '\n')
                for value in self.club_data:
                    csv_file.write(','.join(value.values()) + '\n')

        except IOError:
            print("I/O error")


class Players(object):
    """Uma classe que representa os participantes do Cartola FC.
    Args:
    ----------
    json_data(object): Dados dos players no formato json.

    Attributes:
    ----------
    json_data(object): Dados dos players no formato json.
    processed_data(list): Dados tratados no primeiro nível.
    grouped_data(dict): Dados tratados e organizados.
    """

    def __init__(self, json_data):
        self.json_data = json_data
        self.processed_data = []
        self.grouped_data = {}

    def pre_processing(self, target_data, scout_keys):
        """Filtra os dados selecionados e desempacota os dados
           associados a key ‘scout’.
        Args:
        ----------
        target_data(list): Lista de dados desejados.
        scout_keys(list): Lista de abreviações do scouts do cartola.
        """

        zero_dict = {k: 0 for k in scout_keys}
        for json_obj in self.json_data:
            # Desempacota o dicionário que está guardado na key 'scout'
            d1 = {k: json_obj[k] for k in target_data if k != 'scout'}

            if 'scout' not in target_data:
                self.processed_data.append(d1)
                continue

            temp_d = json_obj['scout']
            if temp_d is not None:
                d2 = {k: temp_d[k] if k in temp_d else 0 for k in scout_keys}
                d1.update(d2)
            else:
                d1.update(zero_dict)

            self.processed_data.append(d1)

    def group_data(self, group_by_key):
        """Agrupa os players pelas keys associadas aos id's.
        Args:
        ----------
        group_by_key(dict): Dicionário que relaciona as keys com os id´s.
        """
        grouping_keys = group_by_key.values()
        self.grouped_data = {v: list() for v in grouping_keys}

        for player in self.processed_data:
            clube_id = player['clube_id']
            key = group_by_key[str(clube_id)]
            self.grouped_data[key].append(player)

    def save_individual_csv(self, save_by_key, dir_path):
        """Salva os arquivos individualmente agrupadas por key.
        Args:
        ----------
        group_by_key(dict): Dicionário que relaciona as keys com os id´s.
        keys Suportadas: Id, nome, abreviacao, nome_fantasia.
        dir_path(str): Caminho do diretório.
        """

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        first_key = list(self.grouped_data.keys())[0]
        csv_columns = list(self.grouped_data[first_key][0].keys())

        for filename in save_by_key:
            data = self.grouped_data[filename]

            _path = dir_path + f'/{filename}.csv'

            with open(_path, 'w', encoding="utf-8") as csv_file:
                csv_file.write(','.join(csv_columns) + '\n')
                for player_data in data:
                    str_player_data = [str(i) for i in player_data.values()]
                    csv_file.write(','.join(str_player_data) + '\n')

    def save_csv(self, path):
        """Salva os arquivos individualmente agrupadas por key.
        Args:
        ----------
        group_by_key(dict): Dicionário que relaciona as keys com os id´s.
        keys Suportadas: Id, nome, abreviacao, nome_fantasia.
        path(str): Caminho do arquivo.
        """

        # Pega as keys de um dicionário padrão
        keys = list(self.grouped_data.keys())
        first_key = keys[0]

        csv_columns = ['grouping_key'] + list(
            self.grouped_data[first_key][0].keys()
        )

        with open(path, 'w', encoding="utf-8") as csv_file:
            csv_file.write(','.join(csv_columns) + '\n')

            for key in keys:

                data = self.grouped_data[key]

                for player_data in data:
                    str_player_data = [str(key)] + [
                        str(i) for i in player_data.values()
                    ]
                    csv_file.write(','.join(str_player_data) + '\n')
