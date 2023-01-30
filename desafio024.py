# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade = input('Cidade: ').upper().strip()
nomediv = cidade.split()
a = nomediv[0] == 'SANTO'
print(a)