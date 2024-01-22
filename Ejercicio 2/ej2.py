lista1 = []
lista2 = []
resultado = []
for num in range(5):
    num1 = int(input("Dame un número para la primera lista: "))
    lista1.append(num1)
for num in range(5):
    num2 = int(input("Dame un número para la segunda lista: "))
    lista2.append(num2)
print(lista1)
print(lista2)
for n1 in lista1:
    for n2 in lista2:
        if n1 == n2:
            resultado.append(n2)
print(resultado)
