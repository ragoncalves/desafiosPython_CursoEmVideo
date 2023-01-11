# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Valor do produto: R$'))
desc = preco - (preco * 0.15)
print('Valor do produto com 15% de desconto: R${:.2f}'.format(desc))