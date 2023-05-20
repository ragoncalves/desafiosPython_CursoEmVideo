# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

list = []
resp = 'Ss'
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    if num not in list:
        list.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')
    resp = input('Quer continuar? [S/N] ').lower().strip()[0]
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        print('Resposta inválida')
        resp = input('Quer continuar? [S/N] ').lower().strip()[0]

print('=' * 40)
print(f'Você digitou os valores: {sorted(list)}')