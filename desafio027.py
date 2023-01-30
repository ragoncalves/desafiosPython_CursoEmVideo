# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

fullname = input('Digite seu nome completo: ')
divname = fullname.split()
print(f'Primeiro nome: {divname[0]}')
print(f'Último nome: {divname[len(divname) - 1]}')