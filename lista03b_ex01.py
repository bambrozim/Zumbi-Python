'''
Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um
inteiro não-negativo n, verificar se n é triangular.
'''
n = int(input("Digite um número inteiro positivo: "))
istriangular = False

for i in range(1,int(n/2)):
    if (i*(i+1)*(i+2))%n == 0:
        istriangular = True
        break

if istriangular == True:
    print("É triangular.")
else:
    print("Não é triangular.")
