# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

numeros = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    resp = input('Quer continuar? [S/N] ').lower().strip()[0]
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        print('Resposta inválida')
        resp = input('Quer continuar? [S/N] ').lower().strip()[0]
        
print(f'Lista completa: {numeros}')
print(f'Números pares digitados: {par}')
print(f'Números ímpares digitados: {impar}')