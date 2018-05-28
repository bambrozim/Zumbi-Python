salario_bruto = float(input("Ganho por horas: "))
horas = float(input("Horas trabalhadas no mês: "))

salario_bruto *= horas
ir = salario_bruto*.11
inss = salario_bruto*.08
sindicato = salario_bruto*.05
salario_liquido = salario_bruto - (ir + inss + sindicato)

print("+Salário Bruto: R$ {0:.2f} \n-IR(11%): R$ {1:.2f} \n-INSS(8%): R$ {2:.2f} \n-Sindicato(5%): R$ {3:.2f} \n=Salário Líquido: R$ {4:.2f}".format(salario_bruto, ir, inss, sindicato, salario_liquido))
