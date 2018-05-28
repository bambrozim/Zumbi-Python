'''
Faça um programa que crie dois vetores com 10 elementos aleatorios entre 1 e 100.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores. Imprima os três vetores.
'''

import random

vetor1 = []
vetor2 = []

for i in range(10):
    n1, n2 = random.randint(1, 100), random.randint(1, 100)
    vetor1.append(n1)
    vetor2.append(n2)

vetor3 = []

for i in range(len(vetor1)):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("vetor 1 =", vetor1)
print("vetor 2 =", vetor2)
print("vetor 3 =", vetor3)
