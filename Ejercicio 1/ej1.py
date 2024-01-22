lista = [12, 23, 5, 29, 92, 64]

lista.pop()
lista.insert(0, 64)
print(lista)
lista.pop(1)
lista.append(12)
print(lista)
lista.insert(0, 14)
print(lista)
sum_total = sum(lista)
lista.append(sum_total)
print(lista)
lista2 = [4, 11, 32]
lista.extend(lista2)
print(lista)
i = 0
while i < len(lista):
    if lista[i] % 2 != 0:
        lista.pop(i)
    else:
        i += 1
print(lista)
lista.sort()
print(lista)
lista.clear()
print(lista)