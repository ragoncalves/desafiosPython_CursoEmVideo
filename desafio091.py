# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 01': randint(1,6),
        'Jogador 02': randint(1,6),
        'Jogador 03': randint(1,6),
        'Jogador 04': randint(1,6)}

ranking = []
print('Dados sorteados:')
print(' ')
sleep(1)

for k, v in jogo.items():
    print(f'{k}: {v}')
    sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)

print('=' * 30)

print('Vencedores em ordem crescente:')
print(' ')

for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0]}')