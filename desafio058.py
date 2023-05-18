# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
n = randint(0 , 10)
num = int(input('Em qual número estou pensando (0 a 10)? '))
palpites = 0
while num != n:
    print('ERROU!!! :(')
    if num < n:
        print('Mais alto!')
    elif num > n:
        print('Mais baixo!')
    num = int(input('Em qual número estou pensando (0 a 10)? '))
    palpites += 1
print(f'Acertou com {palpites + 1} tentativas!!!')