# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
n = randint(1 , 5)
num = int(input('Em qual número estou pensando (0 a 5)? '))
print('Certa a resposta!' if num == n else 'ERROU!!!')