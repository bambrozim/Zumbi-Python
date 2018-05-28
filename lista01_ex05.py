preco = float(input("Preço da mercadoria: "))
desconto_porcentagem = float(input("Porcentagem do desconto: "))

desconto_valor = float(preco*(desconto_porcentagem/100))
preco_final = float(preco - desconto_valor)

print("O desconto foi de R$", desconto_valor, "e o preço final é de R$", preco_final, ".")

