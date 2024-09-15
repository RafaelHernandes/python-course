"""
Listas em Python

Tipo list - Mutável

Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, inset, pop, del, clear, extend, +
Create Read Update Delete
Criar  Ler  Alterar  apagar = lista[i] (CRUD)

String = cadeia de caracteres
"""

#        0  1  2  3
lista = [1, 2, 3, 4]
lista[2] = 300 # Nesse momento o índice 2 da lista vale 300
del lista[2] # Deletando o valor ATUAL do índice 2
print(lista)
print(lista[2]) # Nesse momento você vai conseguir visualizar o valor 4, sendo que lá em cima seria o 300, mas por que? Por quê ao deletar um valor a lista reorganiza os índices
# É de boa prática evitar deletar dados de uma lista, pois em um cenário de escala maior, imagina apagar o índice 2 de uma lista de 10.000 itens? o Python teria que reorganizar
# 9.998 índices..

# Sempre interessante mexer com o final da lista, e no caso de querer adicionar mais valores a lista? utilizando o método append, exemplo:
lista.append(5) # Adicionando o 5
print(lista)
lista.append(6) # Adicionando o 6
print(lista)

# E para remover itens da lista? com o método pop

lista.pop() # remove sempre o ULTIMO valor da lista
print(lista)

# Caso o valor que você queira remover não seja o ultimo índice, basta informar qual índice você quer deletar no pop, exemplo:
lista.pop(2) # Apagando o 4
print(lista)