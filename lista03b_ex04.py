'''
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando tambem a multiplicidade de cada fator.
'''
def isprimo(x):
    for i in range(2, x-1):
        if x%i == 0:
            return False
    return True
    
def proximoprimo(x):
    while True:
        x += 1
        if isprimo(x) == True:
            return x      
        
n = int(input("Digite um número inteiro positivo: "))
fatores = []
contadores = []
if isprimo(n) == True:
    print("O número informado é primo.")
else:
    n_fat = n
    fat = 2
    contador = 1
    while n_fat != 1:
        if n_fat%fat == 0:
            print("%d | %d" %(n_fat, fat))
            n_fat = n_fat/fat
            
            if len(fatores) > 0 and fat == fatores[-1]:
                contadores[-1] += 1
            else:
                fatores.append(fat)
                contadores.append(contador)

        else:
            fat = proximoprimo(fat)
    print("1|")
    print("Foram utilizados o(s) fator(es):")
    for i in range(len(fatores)):
        print("%d - %d vez(es)" %(fatores[i], contadores[i]))