def factorial(a):
    if a == 1:
        return 1
    else:
        return (a * factorial(a - 1))

num = int(input('ingrese un numero entero: '))

factor = factorial(num)
print(num)
print(factor)
