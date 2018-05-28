salario_atual = float(input("Salário atual: "))
aumento_porcentagem = float(input("Porcentagem do aumento: "))

aumento_valor = salario_atual*(aumento_porcentagem/100)
salario_novo = salario_atual + aumento_valor

print("O aumento foi de R$ %.2f e o salário agora é de R$ %.2f." %(aumento_valor, salario_novo))
