# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome

nome = input('Nome: ').lower().split()
print(f'Seu nome tem Silva? {"silva" in nome}')