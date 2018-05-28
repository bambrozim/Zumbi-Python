ano = int(input("Ano: "))
bissexto = 0

if ano%4 == 0:
    bissexto = 1
    if ano%100 == 0:
        bissexto = 0
        if ano%400 == 0:
            bissexto = 1

if bissexto == 1:
    print("É bissexto.")
else:
    print("Não é bissexto.")
