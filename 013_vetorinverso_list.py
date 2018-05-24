vet = []
vet_inv = []
i = 0

while i < 10:
    n = float(input("Digite o %dº número: " %(i + 1)))
    vet.append(n)
    i += 1
print(vet[::-1])
'''
i -= 1

while i >= 0:
    vet_inv.append(vet[i])
    i -= 1

print("Vetor digitado: ", vet)
print("Vetor invertido: ", vet_inv)
'''
