# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatc = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        somatc += matriz[l][2]
        if matriz[1][c] == 0:
            mai = matriz[1][c]
        else:
            if matriz[1][c] > mai:
                mai = matriz[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'Soma de todos os valores pares: {somapar}')
print(f'Soma dos valores da terceira coluna: {somatc}')
print(f'Maior valor da segunda linha: {mai}')