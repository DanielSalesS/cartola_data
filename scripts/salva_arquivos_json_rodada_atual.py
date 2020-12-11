import sys

sys.path.append(r'../')
from cartola.api import ApiClient
from cartola.cartola_settings import dynamic_api, fixed_api

info = ApiClient(url=dynamic_api['status'])
rodada_atual = info.get_data_by_key(key='rodada_atual')
dir_path = fr'json_files/rodada{rodada_atual}'

for url in dynamic_api.values():
    print(url)
    try:
        temp_api = ApiClient(url=url)
        temp_api.save_as_json(dir_path=dir_path, round=rodada_atual)
    except:
        print("Error -->:", url)

print(f"\nDados salvos em: {dir_path}")

input('\nPress Any Key to Continue.')
