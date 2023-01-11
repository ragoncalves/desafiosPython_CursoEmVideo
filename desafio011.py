# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

larg = float(input('Largura em metros: '))
alt = float(input('Altura em metros: '))
metrosquad = larg * alt
tinta = metrosquad * 2
print('Sua parede tem {} m². Você usará {} litros de tinta para pintá-la'.format(metrosquad, tinta))