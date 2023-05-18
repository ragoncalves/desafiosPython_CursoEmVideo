# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

anoatual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}º pessoa nasceu? : '))
    if anoatual - ano >= 18:
        maior += 1
    else:
        menor += 1
        
print(f'Maiores de idade: {maior}\nMenores de idade: {menor}')