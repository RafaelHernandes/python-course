"""
Listas em Python

Tipo list - Mutável

Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, inset, pop, del, clear, extend, +


String = cadeia de caracteres
"""

#        +01234
#        -54321

string = "ACBDE" # 5 caracteres (len)

# lista = list() # Primeira forma de criar uma lista

# lista = [] # Segunda forma de criar, e a mais comum, uma lista vazia

# print(bool([])) # ao comparada com um boolean, quando vazia retorna falsy
# print(lista, type(lista)) 

# Assim como na String, é possível acessar os índices da lista, porém não acessamos letra por letra e sim um item por item, exemplo:
#         0     1          2           3    4       
lista = [123, True, "Rafael Ricardo", 1.2, []]
#        -5    -4         -3          -2   -1
print(lista[2]) # Acessamos o "Rafael Ricardo" com o índice 2 ou com o -3
lista[2] = "João" # Mostrando como é mutável a lista
print(lista[2]) # podendo acessar com 2 ou -3