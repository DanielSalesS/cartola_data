''''Dados, constantes e configurações do Cartola.
    Base 2020.'''

# Os clubes que estão atualmente no Campeonato Brasileiro — Série A
clubs = [
    'Flamengo',
    'Botafogo',
    'Corinthians',
    'Bahia',
    'Fluminense',
    'Vasco',
    'Palmeiras',
    'São Paulo',
    'Santos',
    'Bragantino',
    'Atlético-MG',
    'Grêmio',
    'Internacional',
    'Goiás',
    'Sport',
    'Athlético-PR',
    'Coritiba',
    'Ceará',
    'Fortaleza',
    'Atlético-GO',
]

# id´s dos clubes
club_ids = [
    '262',
    '263',
    '264',
    '265',
    '266',
    '267',
    '275',
    '276',
    '277',
    '280',
    '282',
    '284',
    '285',
    '290',
    '292',
    '293',
    '294',
    '354',
    '356',
    '373',
]

scouts = [
    'Desarme',
    'Falta Cometida',
    'Gol Contra',
    'Cartao Amarelo',
    'Cartao Vermelho',
    'Jogo sem sofrer gol',
    'Defesa Dificil',
    'Defesa de Penalti',
    'Gol Sofrido',
    'Falta Sofrida',
    'Passe Incompleto',
    'Assistencia',
    'Finalizacao na Trave',
    'Finalizacao defendida',
    'Finalização pra Fora',
    'Gol',
    'Impedimento',
    'Penalti Perdido',
]

# Abreviação dos scouts
scout_keys = [
    'RB',
    'FC',
    'GC',
    'CA',
    'CV',
    'SG',
    'DD',
    'DP',
    'GS',
    'FS',
    'PI',
    'A',
    'FT',
    'FD',
    'FF',
    'G',
    'I',
    'PP',
]

# Pontuação de cada scout
score = [
    1.0,
    -0.5,
    -5.0,
    -2.0,
    -5.0,
    5.0,
    4.0,
    7.0,
    -2.0,
    0.5,
    -0.1,
    5.0,
    3.0,
    1.2,
    0.8,
    8.0,
    -0.5,
    -4.0,
]

target_data = [
    'nome',
    'slug',
    'apelido',
    'foto',
    'atleta_id',
    'rodada_id',
    'clube_id',
    'posicao_id',
    'status_id',
    'pontos_num',
    'preco_num',
    'variacao_num',
    'media_num',
    'jogos_num',
    'scout',
]

# Dados atualizados a cada rodada
dynamic_api = {
    'status': 'https://api.cartolafc.globo.com/mercado/status',
    'atletas_mercado': 'https://api.cartolafc.globo.com/atletas/mercado',
    'mercado_destaques': 'https://api.cartolafc.globo.com/mercado/destaques',
    'atletas_pontuados': 'https://api.cartolafc.globo.com/atletas/pontuados',
    'pontos_destaques': 'https://api.cartolafc.globo.com/pos-rodada/destaques',
    'partidas': 'https://api.cartolafc.globo.com/partidas',
}

# Dados fixos
fixed_api = {
    'clubes': 'https://api.cartolafc.globo.com/clubes',
    'patrocinadores': 'https://api.cartolafc.globo.com/patrocinadores',
    'rodadas': 'https://api.cartolafc.globo.com/rodadas',
    'clubes': 'https://api.cartolafc.globo.com/clubes',
}
