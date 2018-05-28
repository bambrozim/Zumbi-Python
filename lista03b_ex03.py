'''
Verifique se um inteiro positivo n é primo.
'''
n = int(input("Digite o número: "))

isprimo = True

for i in range(2, n-1):
    if n%i == 0:
        isprimo = False
        break

if isprimo == True:
    print("É primo.")
else:
    print("Não é primo.")
