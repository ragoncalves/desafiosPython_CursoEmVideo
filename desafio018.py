# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan

n = float(input('Número: '))
print(f'Seno: {sin(n)}\nCosseno: {cos(n)}\nTangente: {tan(n)}')