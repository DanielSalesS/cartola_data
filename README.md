# Cartola Data


## 💻 Sobre o projeto

Cartola Data é um sistema de extração, limpeza e organização dos dados da API do Cartola FC.


## Demonstração

### Informações dos clubes
```python
api_cartola = ApiClient(url='https://api.cartolafc.globo.com/clubes')
club_info = api_cartola.get_json()
club_data = Clubs(json_data=club_info)

# Dados desejados.
target_data = ['id', 'nome', 'abreviacao', 'nome_fantasia']

# Obtém os dados desejados.
club_data.club_information(club_ids=club_ids, target_data=target_data)

dir_path = r'clubes'
# Salva os dados no formato csv.
club_data.save_as_csv(path=dir_path + r'/dados_dos_clubes.csv')

```
Resultado:

|id |nome       |abreviacao|nome_fantasia|
|---|-----------|----------|-------------|
|262|Flamengo   |FLA       |Flamengo     |
|263|Botafogo   |BOT       |Botafogo     |
|264|Corinthians|COR       |Corinthians  |
|265|Bahia      |BAH       |Bahia        |




### Dados dos jogadores

Rodando o script.

![](https://github.com/DanielSalesS/teste1/blob/main/pasta1/script.gif)



## Tutoriais
- [Extrair, selecionar e salvar os dados da API do Cartola.](https://github.com/DanielSalesS/cartola_data/blob/main/notebooks/api_client.ipynb)
- [Obter dados dos clubes.](https://github.com/DanielSalesS/cartola_data/blob/main/notebooks/dados_dos_clubes.ipynb)
- [Obter, filtrar e salvar os dados dos jogadores.](https://github.com/DanielSalesS/cartola_data/blob/main/notebooks/dados_dos_jogadores.ipynb)
- [Obter dados de uma rodada antiga.](https://github.com/DanielSalesS/cartola_data/blob/main/notebooks/dados_de_uma_rodada_antiga.ipynb)



## Dados atualizados de 2020.
- [Dados dos jogadores.](https://github.com/DanielSalesS/cartola_data/tree/main/csv_files)
- [Arquivos JSON das rodadas antigas.](https://github.com/DanielSalesS/cartola_data/tree/main/json_files)

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

