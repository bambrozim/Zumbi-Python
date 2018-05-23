n = int(input("Digite um número inteiro a ser gerado o fatorial: "))
i = n
fat = 1

while i >= 1:
    fat *= i
    i -= 1

print("%d! = %d" %(n, fat))
