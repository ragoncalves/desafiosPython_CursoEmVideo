# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato

soma = maior1000 = menor = cont = 0
barato = ''

while True:
    print('-'*27)
    print('    LOJA SUPER BARATÃO')
    print('-'*27)
    
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    
    soma += preco
    
    if preco > 1000:
        maior1000 += 1 
        
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
    if resp == 'N':
        break
    
print('{:-^40}'.format(' FIM DO PROGRAMA '))
    
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {maior1000} produtos custando mais de R$ 1000,00')
print(f'Produto mais barato: {produto} | R$ {menor:.2f}')