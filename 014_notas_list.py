notas = []
i = 0
soma = 0

while i < 4:
    notas.append(float(input("Digite a %dª nota: " %(i + 1))))
    soma += notas[i]
    i += 1

print("As notas digitadas foram: ", notas)
print("Média: %.2f" %(soma/4))
