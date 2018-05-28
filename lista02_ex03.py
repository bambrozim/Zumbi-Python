peso = float(input("Peso: "))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso*4

print("Excesso: %.2f kg e Multa: %.2f reais" %(excesso, multa))    
