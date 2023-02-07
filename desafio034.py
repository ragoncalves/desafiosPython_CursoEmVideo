# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Salário R$: '))
print(f'Seu novo salário é R${salario * 1.10:.2f}' if salario > 1250 else f'Seu novo salário é R${salario * 1.15:.2f}')