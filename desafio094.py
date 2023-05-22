# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
        
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    
    galera.append(pessoa.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    
    if resp == 'N':
        break
    
print('=' * 60)    

print(f'Pessoas cadastradas: {len(galera)}')

media = soma / len(galera)
print(f'Média das idades: {media:5.1f} anos')

print('Mulheres cadastradas: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='; ')
print()
    
print('Pessoas acima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k}: {v}; ', end='')

print()
print('<< ENCERRADO >>')