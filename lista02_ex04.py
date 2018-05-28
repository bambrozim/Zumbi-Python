numeros = []

for i in range (3):
    n = int(input("Digite o %dº número: " %(i + 1)))
    numeros.append(n)

numeros.sort()
print("O maior número é %d." %numeros[-1])
