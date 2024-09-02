"""
Tipo List - Mutável

Métodos da lista:

append: Adiciona um item ao final da lista ( aula 49 )
insert: Adiciona um item no índice escolhido ( aula 50 )
pop: Remove do final ou do índice escolhido ( aula 49 )
del: apaga um índice ( aula 49 )
clear: limpa a lista ( aula 50 )
extend: estende a lista
+ -: concatena listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # Concatenando a  lista
print(lista_c)

# Método extend:

lista_a.extend(lista_b) # Estende os valores da lista_a dentro da lista_b
print(lista_a)