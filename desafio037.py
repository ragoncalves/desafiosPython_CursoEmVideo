# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
    [1] Binário
    [2] Octal
    [3] Hexadecimal''')
opcao = int(input('Opção: '))

if opcao == 1:
    print(bin(n)[2:])
elif opcao == 2:
    print(oct(n)[2:])
elif opcao == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida!')