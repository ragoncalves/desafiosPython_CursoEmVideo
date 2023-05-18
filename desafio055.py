# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Informe o {i}º peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
        
print(f'Maior peso lido: {maior:.1f} kg')
print(f'Menor peso lido: {menor:.1f} kg')