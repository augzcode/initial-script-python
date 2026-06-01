# 4) Elaborar um programa para uma loja que possui uma lista contendo a quantidade de itens em estoque
# para diversos produtos. Crie um programa que o usuário deva preencher o nome dos produtos e quantidade
# deste produto (uma lista para o nome e uma lista para quantidade). Classifique cada item como: "Estoque
# crítico" (quantidade menor que 5) ou "Estoque baixo" (entre 5 e 10) ou "Estoque normal" (acima de 10). Gere
# uma nova lista contendo apenas os produtos com estoque crítico. Exiba essa lista ao final.

l1 = []

for x in range(5):
    l1.append(str(input("comidas:")))

print(l1)
l2 = []

for x in l1:
    n1 = float(input(f"digite a quantidade no estoque em KG {x}:"))
    l2.append(n1)

print(l2)

for x in range(len(l1)):
        if l2[x] < 5:
            print(f"{l1[x]}, estoque critico")
        elif l2[x] >= 5 and l2[x] < 10:
            print(f"{l1[x]}, estoque baixo")
        elif l2[x] > 10:
            print(f"{l1[x]}, estoque normal")

l3 = []

for x in range(len(l1)):
    if l2[x] < 5:
        print(f"{l1[x]}: estoque crítico")
        l3.append(l1[x])
    elif l2[x] < 10:
        print(f"{l1[x]}: estoque baixo")
    else:
        print(f"{l1[x]}: estoque normal")

print(f"produtos com estoque crítico: {l3}")
