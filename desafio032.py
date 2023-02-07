# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

ano = int(input('Informe o ano (0 caso queira o ano atual): '))

if ano == 0:
    ano = date.today().year

print(f'{ano}: Ano Bissexto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f'{ano}: Não é ano bissexto')