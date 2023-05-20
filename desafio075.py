# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num[0]}, {num[1]}, {num[2]} e {num[3]}.')
x = num.count(9)
print(f'O valor 9 apareceu {x} vez.') if x == 1 else print(f'O valor 9 apareceu {x} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores PARES digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')