# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário: R$ '))
tempo_pagamento = int(input('Dividir em quantas vezes: '))

mensal = valor_casa / tempo_pagamento
valor_permitido = (salario / 10) * 3

if mensal > valor_permitido:
    print(f'EMPRÉSTIMO NEGADO!\n\nMotivo: Prestação excede 30% do salário.\nPrestação: R$ {mensal:.2f}\nSalário: R$ {salario:.2f}')
else:
    print('EMPRÉSTIMO APROVADO!')