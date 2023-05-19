# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

print('='*40)
print('          GERADOR DE PA          ')
print('='*40)

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
termo = n1
c = 1

while c <= 10:
    print(f'{termo} → ',end='')
    termo += n2
    c += 1
    
print('FIM')