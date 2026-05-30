import biblioteca

#ex1

n1 = int(input("digite um numero:"))
print(biblioteca.dobro(n1))

#ex2
n1 = float(input("digite um numero:"))
print(biblioteca.check(n1))

#ex3
a = int(input("digite o parametro A:"))
b = int(input("digite o parametro B:"))
c = int(input("digite o parametro C:"))
biblioteca.bhaskara(a, b, c)

#ex4
c1 = float(input("digite a temperatura em graus Celsius:"))
biblioteca.fahrenheit(c1)

#ex5
c1 = float(input("digite a temperatura em graus Celsius:"))
print(biblioteca.kelvin(c1))

#ex6
n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segunda numero:"))
print("A=soma. B=subtração. C=multiplicar. D=dividir. E=raiz quadrada(1 numero)")
p = (input("digite o parametro desejado:"))
biblioteca.escolha(n1, n2, p)

#ex7
n1 = int(input("digite um numero:"))
print(biblioteca.primo(n1))
