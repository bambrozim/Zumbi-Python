vetor = []
i = 0
cont = 0

while i < 10:
    n = str(input("Digite o %dº caractere: " %(i + 1)))
    vetor.append(n)
    i += 1

i -= 1

while i >= 0:
    if vetor[i] not in "aeiou":
        cont += 1
    i -= 1
   
print("Foram lidas %d consoantes." %cont)
