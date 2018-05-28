'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor,
sem usar as funções max e min.
'''
import random

lista = []

for i in range(10):
    n = random.randint(1, 100)
    lista.append(n)

lista.sort()
print("O maior valor é %d e o menor valor é %d." %(lista[-1], lista[0]))
