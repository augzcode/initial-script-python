#ex1

def dobro(n1:int):
    '''
    retorna o dobro de n1
    '''
    resultado = n1 * 2
    return int(resultado)

#ex2

def check(n1:float):
    '''
    retorna "1" se positivo "-1" se negativo e "0" se for "0"
    '''
    if n1 >= 1:
        resultado = 1
        return float(resultado)
    elif n1 <= -1:
        resultado = -1
        return float(resultado)
    elif n1 == 0:
        resultado = 0
        return float(resultado)
    
#ex3

def bhaskara(a:int, b:int, c:int):
    '''
    retorna a bhaskara dos parametros a, b, c
    '''
    x1= (-b+(b**2-4*a*c)**0.5) / 2*a
    x2= (-b-(b**2-4*a*c)**0.5) / 2*a
    print(f"calculo de bhaskara:{x1}, {x2}")

#ex4

def fahrenheit(c1:float):
    '''
    retorna a temperatura de celsius para fahrenheit
    '''
    f = (9*c1+160) / 5
    print(f"temperatura em Fahrenheit:{f}")

#ex5

def kelvin(c1:float):
    '''
    retorna a temperatura de celsius para kelvin
    '''
    k = c1 + 273.15
    return float(k)

#ex6

def escolha (n1:int, n2:int, p:str):
    '''
    retorna valor de um numero a partir de escolha
    '''
    if p.lower() == "a" or p.lower() =='soma':
        print(n1 + n2)
    elif p.lower() == 'b' or p.lower() == 'subtração':
        print(n1-n2)
    elif p.lower() == 'c' or p.lower() == 'multipicar':
        print(n1*n2)
    elif p.lower() == 'd' or p.lower() == 'dividir':
        print(n1/n2)
    elif p.lower() == 'e' or p.lower() == 'raiz quadrada' or p.lower() == 'raiz quadrada(1 numero)':
        print(n1**0.5)

#ex7

def primo (n1: int):
    for x in range(1, n1**0.5 + 1):
        if n1 % x == 0:
            resultado = print("primo")
        else:
            resultado = print("nao primo")
    return resultado
