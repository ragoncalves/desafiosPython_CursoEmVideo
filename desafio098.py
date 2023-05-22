# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada

from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    print('=' * 35)
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(1)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    
contador(1, 10, 1)
contador(10, 0, 2)

print('Personalize a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(ini, fim, passo)