dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

print("%d segundos ao total." %(segundos + minutos*60 + horas*3600 + dias*86400))
