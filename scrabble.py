def calcular_valor(palabra):
    contador = 0
    for i in palabra:
        if ord('z') >= ord(i) >= ord('a'):
            num = ord(i) - 97
            contador = contador + POINTS[num]
        elif ord('Z') >= ord(i) >= ord('A'):
            num = ord(i) - 65
            contador = contador + POINTS[num]
        else:
            contador = contador + 0
    return contador


# ESCALA DE VALORES DEL SCRABBLE:
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# INGRESO DE PALABRAS MEDIANTE TECLADO:
PALABRA1 = input('primer jugador: ')
PALABRA2 = input('segundo jugador: ')

valor1 = calcular_valor(PALABRA1)
valor2 = calcular_valor(PALABRA2)

if valor1 > valor2:
    print('Gana el jugador 1')
elif valor1 < valor2:
    print('gana el jugador 2')
else:
    print('empate')

print(valor1)
print(valor2)
