'''
1)
Elaborar um programa que crie um arquivo chamado cidades.txt e grave nele o nome de pelo menos 5 cidades diferentes, uma cidade por linha.
'''
arquivo = open("dados.txt", "w")
for x in range(5):
    cidade = (input("digite uma cidade:"))
    arquivo.write(cidade + "\n")

arquivo.close()

'''
2)
Elaborar um programa que abra o arquivo cidades.txt,
leia todas as cidades cadastradas e exiba uma por uma na tela. Exibir também a quantidade total de cidades cadastradas.
'''
with open("dados.txt", "r") as arquivo:
    cidades=arquivo.readlines()

for k in cidades:
    print(k)

print(f"Existem {len(cidades)} cidades!!")

'''
3)
Elaborar um programa que permita adicionar novas cidades ao arquivo cidades.txt sem apagar as cidades já existentes.
'''
arquivo = open("dados.txt", "a")
novas_cidades= (input("digite uma nova cidade:"))
arquivo.write(novas_cidades + "\n")
arquivo.close()

'''
4)
Complementar o exercício anterior, onde o usuário pode cadastrar várias cidades que o usuário desejar sair.
'''

with open("dados.txt", "a") as arquivo:
    opcao = "s"
    while opcao.lower() == "s":
        cidades = (input("digite uma nova cidade:"))
        arquivo.write(cidades + "\n")
        opcao = (input("deseja continuar(s/n):"))

'''
5)
Elaborar um programa que solicite ao usuário o nome de uma cidade e verifique se ela existe no arquivo cidades.txt.
Ignorar letras maiúsculas e minúsculas na busca.
'''

file = open("dados.txt", "r")
lista = []

for h in file:
    h = h.strip()
    lista.append(h)

busca = (input("Digite a cidade que deseja verificar:"))

if lista.count(busca) == 1:
    print("ESSA CIDADE EXISTE")
else:
    print("ESSA CIDADE NAO EXISTE!!!!!!!!!!!")
file.close()

'''
6)
Elaborar um sistema simples de cadastro de produtos (usuário cadastra) em um arquivo chamado produtos.txt.
Cada linha deve conter: código, nome do produto, categoria, preço. Os dados devem ser separados por ponto e vírgula (;).
Exibir todos os produtos cadastrados formatados na tela.
'''
file = open("produtos.txt", "w")

cod = (input("digite o codigo do produto:"))
nome = (input("digite o nome do produto:"))
cat = (input("digite a categoria do produto:"))
preco = (input("digite o preco do produto:"))

file.write(cod)
file.write(";")
file.write(nome)
file.write(";")
file.write(cat)
file.write(";")
file.write(preco)


file.close()

'''
7)
Elaborar um programa que leia um arquivo chamado alunos.txt contendo: RGM, nome, curso, média.
O programa deve exibir apenas os alunos com média superior a 8.
'''
alunos= [
    [100, "manuela", "SI", 6.7],
    [101, "patricia", "Engenharia de software", 5],
    [102, "amanda", "direito", 7],
    [103, "paulo", "culinaria", 10],
    [104, "fernanda", "psicologia", 3.3]
]

arquivo = open("alunos.txt", "w")
for aluno in alunos:
    if aluno[3] >= 7:
        arquivo.write(f'{aluno[0]};{aluno[1]}; {aluno[2]}; {aluno[3]}\n')

arquivo.close()

'''
8)
Elaborar um programa que solicite um RGM e realize a busca do aluno no arquivo alunos.txt. Caso o aluno exista, exibir todos os seus dados.
'''

file = open("alunos.txt", "r")
lista= []

for h in file:
    h = h.strip()
    lista.append(h)

busca = input("digite um RGM:")

if lista.index() > 0:
    print()



file.close()
