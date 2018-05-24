entrada = str(input("Digite a data de nascimento no formato dd/mm/aaaa: "))
dia, mes, ano = entrada.split("/")
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro"]
n = int(mes) - 1


print("Você nasceu em: %s de %s de %s." %(dia, meses[n], ano))
