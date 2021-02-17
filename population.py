años = 0
comienzo = int(input('ingrese el numero de llamas: '))
while comienzo < 9:
    comienzo = int(input('ingrese el numero de llamas: '))

fin = int(input('numero de llamas al final: '))

while fin < comienzo:
    fin = int(input('numero de llamas al final: '))

num_llamas = comienzo

while num_llamas < fin:
    num_llamas = num_llamas + int(num_llamas/3) - int(num_llamas/4)
    años += 1
print('necesita un total de ' + str(años) + ' años')
