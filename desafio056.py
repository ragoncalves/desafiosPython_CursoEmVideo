# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

idadetotal = 0
imaisvelho = 0
mulher_20 = 0
nmaisvelho = ''

for i in range(1, 5):
    print(f'---------- {i}º Pessoa ----------')
    nome = input(f'Nome: ').title().strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo (M/F): ').upper().strip()
    
    idadetotal += idade
    
    if idade > imaisvelho and sexo == 'M':
        imaisvelho = idade
        nmaisvelho = nome
        
    if idade < 20 and sexo == 'F':
        mulher_20 += 1
    
media = idadetotal / 4

print(f'Média de idade do grupo: {media:.2f}')
print(f'Homem mais velho: {nmaisvelho} ({imaisvelho} anos)')
print(f'Quantas mulheres com menos de 20 anos de idade: {mulher_20}')