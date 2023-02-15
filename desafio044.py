# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: – à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros

preco = float(input('Preço do produto: R$ '))

print('''Forma de Pagamento:
    [1] A vista (Dinheiro)
    [2] A vista (Cartão)
    [3] 2x
    [4] 3x ou mais''')

opcao = int(input('Opção: '))

if opcao == 1:
    print(f'Preço final: R$ {preco * 0.9:.2f}')
elif opcao == 2:
    print(f'Preço final: R$ {preco * 0.95:.2f}')
elif opcao == 3:
    print(f'2x de R$ {preco / 2}')
    print(f'Preço final: R$ {preco}')
elif opcao == 4:
    x = int(input('Quantas vezes: '))
    print(f'{x}x de {(preco * 1.2) / x:.2f}')
    print(f'Preço final: R$ {preco * 1.2:.2f}')
else:
    print('Opção Inválida')