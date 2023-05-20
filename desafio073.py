# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('='*110)
print(f'Lista de tims do brasileirão 2022: {times}')
print('-'*110)
print(f'Os cinco primeiros: {times[0:5]}')
print('-'*110)
print(f'Os quatro últmos: {times[-4:]}')
print('-'*110)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*110)
print(f'O Atlético-MG está na {times.index("Atlético-MG")+1}ª posição.')
print('='*110)