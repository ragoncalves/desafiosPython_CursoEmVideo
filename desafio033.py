#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

menor = a

if b < a and b < c:
    menor = b
    
if c < a and c < b:
    menor = c
    
maior = a

if b > a and b > c:
    maior = b
    
if c > a and c > b:
    maior = c
    
print(f'Maior: {maior}\nMenor: {menor}')