'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR
e os números ímpares na lista IMPAR. Imprima as três listas.
'''
import random

lista = []

for i in range(20):
    n = random.randint(1, 100)
    lista.append(n)

par = []
impar = []

for i in lista:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("lista =", lista)
print("PAR =", par)
print("IMPAR =", impar)
