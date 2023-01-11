# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

reais = float(input('Quantos R$ tem na carteira: R$'))
print('Você pode comprar ${:.2f}'.format(reais * 3.27))