n = 1
soma = 0

while n <= 10:
    x = int(input("Digite o %dº número: " %n))
    soma += x
    n += 1

print("A média é: %.2f" %(soma/10))
