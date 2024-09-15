"""
Desempacotamento em chamdas

de métodos e funções

"""

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"

p,*_, u = lista # Declaro o primeiro valor como "p", o meio como resto e o ultimo como "u"
print(p, u) # Nesse caso estou exibindo o Primeiro valor da lista, que seria "Maria" e o ultimo valor que seria "Eduarda"

# Utilizando o desempacotamento com a função *, todos os elementos de acordo com o tipo de dado, é desempacotado.

print("Maria", "Helena", 1, 2, 3, "Eduarda") # Só pra dar exemplo para o *lista, que seria a mesma coisa
print(*lista) # Desempacota cada índice da lista e printa eles
print(*string) # Desempacota a string, definindo que cada índice corresponde a cada letra nesse caso.
print(*tupla) # Desempacota a tupla que seria cada índice, as suas respectivas palavras

# Exemplos de exibição, caso você queira ver cada dado em uma linha, exemplo podemos usar a função sep="", exemplo:

print(*lista, sep="\n") # Chamamos a lista desempacotada e atribuimos a ela um separador, e o separador é o "\n", que corresponde a quebra de linha