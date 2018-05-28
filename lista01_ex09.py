km = float(input("Km rodados: "))
dias = int(input("Dias alugados: "))

preco = 60*dias + .15*km

print("Preço a pagar: R$ %.2f." %preco)
