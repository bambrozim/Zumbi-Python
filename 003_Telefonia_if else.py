minutos = int(input("Minutos utilizados: "))

if minutos < 0:
    print("Digite uma quantia válida!")
else:
    if minutos < 200:
        conta = .2*minutos
    elif minutos <= 400:
        conta = .18*minutos
    elif minutos <= 800:
        conta = .15*minutos
    else:
       conta = .8*minutos

    print("Sua conta é de R$ %.2f reais." %conta)
