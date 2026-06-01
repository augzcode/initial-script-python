'''
1) Elaborar um programa que o usuário deve digitar 10 números inteiros (esses números
devem ser armazenados em uma lista) e ao final o programa deve mostrar quantos números
são pares e quantos são ímpares.
'''

lista = []
l2 = []
l3 = []

for x in range(10):
    n1 = int(input("digite um numero:"))
    lista.append(n1)
    if n1 % 2 == 0:
        l2.append(n1)
    else:
        l3.append(n1)

print(f"quantidade de numeros pares presente: {len(l2)}")
print(f"quantidade de numeros impares presente: {len(l3)}")

'''
2) Elaborar um programa que o usuário deve digitar 8 números reais (esses números devem 
ser armazenados em uma lista) e depois o programa deve mostrar: todos os números 
digitados, o maior número, o menor número e a diferença entre o maior e o menor valor.
'''

l1 = []

for x in range(8):
    n1 = float(input("digite um numero:"))
    l1.append(n1)

print(l1)
print()

print(f"o valor maximo que esta na lista:{max(l1)}")
print(f"o valor minimo que esta na lista:{min(l1)}")
print()

print(f"a diferenca entre o maior e o menor valor:{max(l1) - min(l1)}")

'''
3) Elaborar um programa que o usuário deve digitar 12 números inteiros (esses números 
devem ser armazenados em uma lista) e em seguida o programa deve mostrar: todos os 
números positivos (armazenados em outra lista), todos os números negativos
(armazenados em outra lista), a quantidade de zeros digitados.
'''

l1 = []
l2 = []
z = 0
for x in range(12):
    n1 = int(input("digite um numero:"))
    if n1 > 0:
        l1.append(n1)
    elif n1 < 0:
        l2.append(n1)
    else:
        z += 1
print(f"sua lista de numeros positivos: {l1}")
print(f"sua lista de numeros negativos: {l2}")
print()
print(f"quantidade de zeros:{z}")

'''
4) Elaborar um programa que o usuário deve digitar 7 nomes de alunos (esses nomes devem 
ser armazenados em uma lista) e ao final o programa deve mostrar: todos os nomes, o 
primeiro nome digitado, o último nome digitado e quantos nomes possuem mais de 5 letras.
'''
l1 = []
g = 0
for x in range(7):
    n1 = str(input(f'Digite o nome do aluno {x}:'))
    l1.append(n1)
    if len(n1) > 5:
        g += 1
print(f'lista dos nomes de alunos:{l1}')
print()
print(f'primero aluno digitado:{l1[0]}')
print()
print(f'ultimo aluno digitado:{l1[-1:]}')
print()
print(f' nomes que possuem mais de 5 letras:{g}')

'''
5) Elaborar um programa que o usuário deve digitar 15 números inteiros (esses números 
devem ser armazenados em uma lista). Depois o programa deve mostrar: quantas vezes o 
número 10 apareceu e em quais posições o número 10 foi encontrado.
'''

l1 = []
for x in range(15):
    n1 = int(input("digite um numero:"))
    l1.append(n1)
print(f"a quantidade de numero '10' presente na lista: {l1.count(10)}")
i = 0
for x in l1:
    if x == 10:
        print(f"posição dos numeros 10 encontrados:{i}")
    i += 1
