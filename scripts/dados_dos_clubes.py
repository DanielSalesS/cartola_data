import json
import path_config
from cartola.api import ApiClient
from cartola.processdata import Clubs
from cartola.cartola_settings import club_ids


api_cartola = ApiClient(url='https://api.cartolafc.globo.com/clubes')
club_info = api_cartola.get_json()

club_data = Clubs(json_data=club_info)

# Dados desejados
target_data = ['id', 'nome', 'abreviacao', 'nome_fantasia']

# Obtém os dados desejados.
club_data.club_information(club_ids=club_ids, target_data=target_data)
dir_path = r'clubes'
# Salva dos dados no formato json.
club_data.save_as_json(path=dir_path + r'/dados_dos_clubes.json')
print(dir_path + r'/dados_dos_clubes.json')
# Salva dos dados no formato csv.
club_data.save_as_csv(path=dir_path + r'/dados_dos_clubes.csv')

print(f"\nDados salvos em: {dir_path}")

input('\nPress Any Key to Continue.')
