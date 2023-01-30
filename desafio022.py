# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome

fullname = input('Nome completo: ').strip()
print('Nome todo em maiúsculo: {}'.format(fullname.upper()))
print('Nome todo em minúsculo: {}'.format(fullname.lower()))
print('Total de letras sem contar espaços: {}'.format(len(fullname) - fullname.count(' ')))
print('Total de letras do primeiro nome: {}'.format(fullname.find(' ')))