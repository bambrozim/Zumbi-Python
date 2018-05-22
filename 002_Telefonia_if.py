minutos = int(input("Minutos utilizados: "))
conta = 0

if minutos < 0:
    print("Digite uma quantia válida")
if minutos >= 0 and minutos < 200:
    conta += .2*minutos
    print("Utilizou menos de 200 minutos, conta é de R$ %.2f reais." %conta)
if minutos >= 200 and minutos <= 400:
    conta += .18*minutos
    print("Utilizou entre 200 a 400 minutos, conta é de R$ %.2f reais." %conta)
if minutos > 400:
    conta += .15*minutos
    print("Utilizou mais de 400 minutos, conta é de R$ %.2f reais." %conta)
    
