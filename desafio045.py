# Crie um programa que faça o computador jogar Jokenpô com você

from random import choice

print('='*16)
print('    Jokenpô')
print('='*16)
print('')

user_option = input('Pedra, Papel ou Tesoura? ').title().strip() 

pc = ['Pedra', 'Papel', 'Tesoura']
pc_option = choice(pc)
print(f'Computador: {pc_option.title()}\n')

if user_option == pc_option:
    print('Empate!')
elif user_option == 'Pedra' and pc_option == 'Tesoura':
    print('VOCÊ VENCEU!!! :D')
elif user_option == 'Tesoura' and pc_option == 'Papel':
    print('VOCÊ VENCEU!!! :D')
elif user_option == 'Papel' and pc_option == 'Pedra':
    print('VOCÊ VENCEU!!! :D')
else:
    print('Você perdeu! :(')