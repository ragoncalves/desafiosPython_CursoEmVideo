# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

pc = randint(0, 11)
c = 0
i = True
title = 'PAR OU IMPAR'

print('=-'*20)
print(f'{title:^40}')
print('=-'*20)

while i == True:
    user = int(input('Digite um valor [0 a 10]: '))
    parouimpar = str(input('Par ou Impar: ')).strip().title()
    total = pc + user
    
    
    if user >= 0 and user <= 10 and parouimpar == 'Par' or parouimpar == 'Impar': 
        if total % 2 == 0 and parouimpar == 'Par':
            print('-'*40)
            print(f'Computador: {pc}\nTotal: {pc + user}\n\nVOCÊ VENCEU!!!')
            c += 1
            print('-'*40)
            
        elif total % 2 == 1 and parouimpar == 'Impar':
            print('-'*40)
            print(f'Computador: {pc}\nTotal: {pc + user}\n\nVOCÊ VENCEU!!!')
            c += 1
            print('-'*40)
        
        else:
            print('-'*40)
            print(f'Computador: {pc}\nTotal: {pc + user}\n\nVOCÊ PERDEU!!!')
            i = False
    else:
        print('\nOpção inválida! Tente novamente.\n')

print(f'GAME OVER! Vitórias: {c}')