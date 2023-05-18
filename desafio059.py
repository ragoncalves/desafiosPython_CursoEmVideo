# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep 
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1
        print(f'{maior} > {menor}')
    
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    
    elif opcao == 5:
        print('Finalizando...')
    
    else:
        print('Opcão inválida. Tente novamente')
    print('=-='* 10)
    sleep(2)

print('Fim do programa!')