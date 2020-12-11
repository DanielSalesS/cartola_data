import sys
import json

sys.path.append(r'../')
from cartola.api import ApiClient
from cartola.cartola_settings import scout_keys, clubs, club_ids, dynamic_api
from cartola.processdata import Players


def read_json(path):
    dados = {}
    try:
        with open(path, 'r', encoding="utf-8") as json_file:
            dados = json.load(json_file)
    except IOError:
        print("I/O error")

    return dados


status = ApiClient(url=dynamic_api['status'])
rodada_atual = status.get_data_by_key(key='rodada_atual')
print(f'Rodada Atual: {rodada_atual}\n')

# A partir da rodada 9
# O script salva_arquivos_json_rodada_atual.py atualiza os dados
rodada = input('Digite uma rodada antiga: ')

path = fr'json_files/rodada{rodada}/atletas_mercado_{rodada}.json'

dir_path = fr'csv_files/rodada{rodada}'

target_data = [
    'clube_id',
    'nome',
    'slug',
    'apelido',
    'atleta_id',
    'rodada_id',
    'posicao_id',
    'status_id',
    'pontos_num',
    'preco_num',
    'variacao_num',
    'media_num',
    'jogos_num',
    'scout',
]

# dados_rodada = ApiClient(url="https://api.cartolafc.globo.com/atletas/mercado")
json_data = read_json(path)
atletas = json_data['atletas']
players = Players(json_data=atletas)
players.pre_processing(target_data=target_data, scout_keys=scout_keys)

# Agrupa jogadores pelas keys associadas aos id's.
group_by_key = {k: value for k, value in zip(club_ids, clubs)}
players.group_data(group_by_key=group_by_key)

# Separa as informações por key e salva separadamente os arquivos.
players.save_individual_csv(save_by_key=clubs, dir_path=dir_path)
# Salva todos os dados em um único arquivo.
players.save_csv(path=dir_path + r'/all_players.csv')

print(f"\nDados salvos em: {dir_path}")

input('\nPress Any Key to Continue.')
