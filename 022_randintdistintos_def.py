import random

def verify(lista, x):
    for i in range(len(lista)):
        if x == lista[i]:
            return 1
    return 0

lista = []

for i in range(15):
    n = random.randint(10, 100)
    while verify(lista, n) == 1:
        n = random.randint(10, 100)

    lista.append(n)

lista.sort()
print(lista)

'''

import random
lista = []
while len(lista) < 15:
    x = random.randit(10, 100)
    if x not in lista:
        lista.append(x)
lista.sort()
print (lista)

'''
