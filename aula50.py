"""
Tipo List - Mutável

Métodos da lista:

append: Adiciona um item ao final da lista ( aula 49 )
insert: Adiciona um item no índice escolhido
pop: Remove do final ou do índice escolhido ( aula 49 )
del: apaga um índice ( aula 49 )
clear: limpa a lista
extend: estende a lista
+ -: concatena listas
"""

lista = [10, 20, 30, 40]
lista.append(1234)
print(lista)
# o método del apaga um item de uma lista, mas como deletar o ultimo valor? fazemos isso usando um índice invertido, exemplo:
del lista[-1]
# lista.clear() - limpa a lista por completo
print(lista) 
# Para adicionar um novo item a lista, em um índice de sua escolha, utilizamos o insert, exemplo:
lista.insert(0, 5) # o Insert recebe dois parâmetros, o primeiro é o índice e o segundo qualquer tipo de dados/valor
print(lista)