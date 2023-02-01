# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

vel = int(input('Velocidade atual (km/h): '))
print(f'{vel} km/h: Velocidade permitida!' if vel <= 80 else f'Você foi multado em R$ {(vel-80)*7:.2f}')