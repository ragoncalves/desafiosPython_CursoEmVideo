# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')