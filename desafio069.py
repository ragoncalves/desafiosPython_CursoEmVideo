# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos

idade = pessoas_maior_18 = mulheres_menor_20 = homens = 0

while True:
    print('-'*27)
    print('    CADASTRE UMA PESSOA')
    print('-'*27)
    
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').upper().strip()[0]
    
    if idade > 18:
        pessoas_maior_18 += 1
        
    if sexo == 'M':
        homens += 1
        
    if idade < 20 and sexo == 'M':
        mulheres_menor_20 += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    
print('=====FIM DO PROGRAMA=====')    
    
print(f'Total de pessoas com mais de 18 anos: {pessoas_maior_18}')
print(f'Ao todo, temos {homens} homens cadastrados')
print(f'e temos {mulheres_menor_20} mulher com menos de 20 anos')