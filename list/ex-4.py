lista = []
for x in range(5):
    n1 = int(input("digite um numero:"))
    if n1 < 0:
        lista.append(0)
    else:
        lista.append(n1)
print(lista)
