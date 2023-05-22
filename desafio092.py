# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

dados = {}

dados['Nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho [Digite 0 caso não possua]: '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = ((dados['Ano de Contratação'] + 35) - datetime.now().year) + dados['Idade']
    
print('=' * 50)

for k, v in dados.items():
    print(f'{k}: {v}')