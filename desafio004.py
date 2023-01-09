# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

x = input('Digite algo: ')

print('Tipo primitivo:', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculo?', x.isupper())
print('Está em minúsculo?', x.islower())
print('Está capitalizada?', x.istitle())