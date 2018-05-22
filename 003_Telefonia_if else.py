minutos = int(input("Minutos utilizados: "))

if minutos < 0:
    print("Digite uma quantia válida!")
else:
    if minutos >= 0 and minutos < 200:
        conta = .2*minutos
    else:
        if minutos >= 200 and minutos <= 400:
            conta = .18*minutos
        else:
            if minutos > 400 and minutos <= 800:
                conta = .15*minutos
            else:
                conta = .8*minutos

    print("Sua conta é de R$ %.2f reais." %conta)
