def collatz(a, contador=0):
    if a == 1:
        print(a)
        return contador
    elif a % 2 == 0:
        contador += 1
        print(a)
        return collatz(a / 2, contador)
    else:
        contador += 1
        print(a)
        return collatz(3 * a + 1, contador)


num = int(input('ingrese un numero entero: '))
pasos = collatz(num)
print(pasos)
