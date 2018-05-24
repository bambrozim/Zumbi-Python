i = 0
n = [0, 0, 0, 0, 0]
soma = 0

for i in range(5):
    n[i] = int(input("Digite o %dº número: " %(i + 1)))
    soma += n[i]

print("A média é: %.2f." %(soma/5))
