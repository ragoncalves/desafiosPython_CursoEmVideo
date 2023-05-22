# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista

list = []
cont = 0
resp = 'Ss'
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    list.append(num)
    cont += 1
    resp = input('Quer continuar? [S/N] ').lower().strip()[0]
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        print('Resposta inválida')
        resp = input('Quer continuar? [S/N] ').lower().strip()[0]

print(f'Você digitou {cont} valores.')
print(f'Em ordem decrescente: {sorted(list, reverse=True)}')
print ('O valor 5 faz parte da lista.') if 5 in list else print('O valor 5 NÃO faz parte da lista.')