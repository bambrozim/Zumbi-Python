a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))

if a == b and a == c:
    print("Equilatero.")
elif a == b or a == c:
    print("Isosceles.")
else:
    print("Escaleno.")
