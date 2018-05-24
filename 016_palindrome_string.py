texto = str(input("Digite uma palavra ou uma frase: "))

if texto == texto[::-1]:
    print("É palíndrome!")

else:
    print("Não é palíndrome.")
