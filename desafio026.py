# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase = input('Digite uma frase: ').lower().strip()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('a')))
print('Primeiro na posição {}'.format(frase.find('a') + 1))
print('Por último na posição {}'.format(frase.rfind('a') + 1))