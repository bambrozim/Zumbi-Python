import math
area = float(input("Área a ser pintada (m²): "))
litros = area/3
latas = math.ceil(litros/18)
preco_total = latas*80

print("Latas: %d \nCusto total: R$ %.2f" %(latas, preco_total))
