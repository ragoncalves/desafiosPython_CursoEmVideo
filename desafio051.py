# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print('='*40)
print('          10 TERMOS DE UMA PA          ')
print('='*40)

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
dec = n1 + (10 - 1) * n2

for i in range(n1, dec + n2, n2):
    print(f'{i} → ', end = '')
print('ACABOU!')