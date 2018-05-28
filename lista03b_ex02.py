'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler
o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas
esteja em falta no caixa.
'''

conta = int(input("Total da conta: "))
pagamento = int(input("Pagamento: "))
troco = pagamento - conta

notas50 = int(troco/50)
resto = troco%50
notas20 = int((resto)/20)
resto = resto%20
notas10 = int((resto)/10)
resto = resto%10
notas5 = int((resto)/5)
resto = resto%5
notas2 = int((resto)/2)
resto = resto%2
notas1 = int(resto)

print("%d notas de 50 \n%d notas de 20 \n%d notas de 10 \n%d notas de 5 \n%d notas de 2 \n%d notas de 1" %(notas50, notas20, notas10, notas5, notas2, notas1))
