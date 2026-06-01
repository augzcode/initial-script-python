l1 = []

for x in range(1):
    n1 = float(input("digite a temperatura:"))
    while n1 >0:
        l1.append(n1)
        n1 = float(input("digite a temperatura:"))
l2 = []
l3 = []
l4 = []
l5 = []

for x in l1:
    if x < 10:
        print(f"temperatura fria {x}°C")
        l2.append(x)
    elif x > 10 and x < 30:
        print(f"temperatura Agradavel {x}°C")
        l3.append(x)
    elif x > 30 and x < 60:
        print(f"temperatura quente {x}°C")
        l4.append(x)
    else:
        print(f'temperatura nao plausivel {x}°C')
        l5.append(x)

print(f"temperatura fria: {l2}")
print(f"temperatura Agradavel: {l3}")
print(f"temperatura quente: {l4}")
print(f"temperatura nao plausivel: {l5}")
