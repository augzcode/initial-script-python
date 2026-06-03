'''
1) Elaborar um programa que registre em um dicionário o nome de vários setores de uma empresa
como chave e a quantidade de funcionários em cada setor como valor (o usuário deve inserir os
dados). O programa deve identificar e exibir o setor com o maior número de funcionários.
'''

dados = {}

for x in range(3):
    setor = (input("Digite um setor da empresa:"))
    qtd = int(input('Digite a quantidade de funcionarios:'))
    dados[setor]= qtd
    dados.update()

print(dados)
m = list(dados.values())
maior = max(m)

for x, y in dados.items():
    if dados[x] == maior:
        print(f'setor que contem mais funcionario: {x}')




'''
2) Elaborar um programa que cadastre cursos em um dicionário, no qual a chave seja o código do 
curso e o valor seja outro dicionário contendo: nome do curso, carga horária e quantidade de 
vagas. O programa deve permitir consultar os dados de um curso pelo código.
'''

curso = {
    1:{'curso': 'ingles', 'carga horaria': 400, 'vagas': 40},
    2:{'curso': 'judo', 'carga horaria': 280, 'vagas': 25},
    3:{'curso': 'espanhol', 'carga horaria': 350, 'vagas': 35},
    4:{'curso': 'python', 'carga horaria': 650, 'vagas': 50}
}

busca = int(input("digite o codigo do curso que deseja:"))
print(curso[busca])


'''
3) Elaborar um programa que armazene em um dicionário o nome de 5 supermercados como chave 
e uma lista contendo os faturamentos dos últimos 4 meses como valor. O programa deve calcular 
a média de faturamento de cada supermercado
'''
mercado = {
    'atacadão':[2000, 6000, 4500, 5000],
    'assai': [4500, 7000, 2000, 3000],
    'extra':[7000, 4000, 2000, 780],
    'americanas':[3000, 2000, 1000, 1000],
    'k-pricho':[500, 200, 600, 780]
}

for x, y in mercado.items():
    media = sum(y) / len(y)
    print(f'o supermercado {x} teve uma media de faturamento nos ultimos 4 meses de: {media}')

'''
4) Elaborar um programa que cadastre equipamentos de informática em um dicionário, no qual a 
chave seja o número de patrimônio e o valor seja outro dicionário contendo: descrição, setor e 
estado de conservação. O programa deve permitir listar todos os equipamentos cadastrados.
'''

patrimonio = {
    100:{'descrição': 'processador intel', 'setor':'recursos humanos', 'estado de conservação':'bom'},
    101:{'descrição': 'placa mae soyo', 'setor':'tecnologia da informação', 'estado de conservação':'excelente'},
    102:{'descrição': 'placa de video rx 580', 'setor':'administrativo', 'estado de conservação':'pessimo'}
}

busca = int(input("insira o patrimonio do equipamento:"))

if busca in patrimonio.keys():
    for chave, valor in patrimonio[busca].items():
        print(chave, valor, sep=' --> ')
else:
    print("PATRIMONIO INEXISTENTE")

'''
5) Elaborar um programa que cadastre filmes em um dicionário, no qual a chave seja um código 
identificador e o valor seja outro dicionário contendo: título, gênero e duração em minutos. O 
programa deve permitir listar apenas os filmes com duração superior a 120 minutos
'''

movies = {
    2:{'titulo':'up: altas aventuras', 'genero': 'aventura', 'duração': 96},
    4:{'titulo':'super mario galaxy', 'genero': 'animação', 'duração': 98},
    6:{'titulo':'panico 7', 'genero': 'terror', 'duração': 114},
    8:{'titulo':'michael', 'genero': 'cinebiografia', 'duração': 130},
    10:{'titulo':'interestelar', 'genero': 'ficção cientifica', 'duração': 169}
}

busca = int(input("digite o codigo do filme:"))

for x, y in movies[busca].items():
    if x == 'duração':
        if x == 'duração' and y > 120:
            for c, b in movies[busca].items():
                print(c, b, sep= ' --> ')
        elif x == 'duração' and y < 120:
            print('filme com menos de 120 minutos nao serão mostrados')
        else:
            print("filme nao exite!")


