# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

# ------------------ Mapeamento de lista trata-se sobre ter uma nova lista do mesmo tamanho da lista antiga apesar de os valores serem diferentes ------------- #

lista = [] # Lista vazia
for numero in range(10): # Para cada numero, armazena 1 valor do range de 0 a 9 (10 valores) no numero, e adiciona na lista através do lista.append(numero)
    lista.append(numero)
# print(lista)


lista = [ # Aqui usamos a list comprehension aonde atribuimos à ESQUERDA DO FOR o que vai ser atribuido
    numero * 2 
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension

produtos = [ # Lista de Dicionarios
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [ # Nova lista com mapeamento do list comprehension, aonde tudo que está a esquerda do for, é considerado algo que está sendo atribuído
    {**produto, 'preco': produto['preco'] * 1.05} # Linha 29 a esquerda do for
    if produto['preco'] > 20 else {**produto} # Linha 30 a esquerda do for
    for produto in produtos 
]

# print(novos_produtos)
print(*novos_produtos, sep='\n') # Desempacotando a lista do novos_produtos e separando ela por quebra de linha