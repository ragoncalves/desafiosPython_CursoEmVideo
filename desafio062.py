# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos

print('='*40)
print('          GERADOR DE PA          ')
print('='*40)

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão: '))
termo = n1
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} → ',end='')
        termo += n2
        c += 1
        
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')