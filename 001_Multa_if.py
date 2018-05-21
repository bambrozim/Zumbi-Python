speed = int(input("Velocidade do carro em km/h: "))
if speed > 110 and speed < 400:
    print("Você foi multado! HAHAHA")
    fee = int(5*(speed - 110))
    print("Tua multa é de R$ %.2f reais" %fee)
if speed < 0:
    print("Digite um número valido ô espertinho")
if speed >= 400:
    print("HAHAHA falou ai ô barrichelo, digite uma velocidade válida")
if speed >= 0 and speed <= 110:
    print("Você não foi multado, parabéns!")
        
