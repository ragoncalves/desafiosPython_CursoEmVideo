# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-'*36)
print('      Sequência de Fibonacci')
print('-'*36)

n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('~'*36)
print(f'{t1} → {t2}',end ='')

c = 3

while c <= n:
    t3 = t1 + t2
    print(f' → {t3}', end ='')
    t1 = t2
    t2 = t3
    c += 1
print(' → FIM')