# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

list = []
for i in range(0, 5):
    list.append(int(input(f'Digite o valor {i + 1}/5: ')))
    
print(f'Valores digitados: {list}')
    
print(f'O maior número digitado foi o {max(list)} que está na posição {list.index(max(list)) + 1} da lista.')
print(f'O menor número digitado foi o {min(list)} que está na posição {list.index(min(list)) + 1} da lista.')