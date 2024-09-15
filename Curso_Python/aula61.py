"""
Listas de listas e seus índices

"""

salas = [
    #0            1
    ["Maria", "Helena"], #0
    
    #0
    ["Elaine"], #1
    
    #0          1        2
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)]  #2
]

# print(salas)
# # Como acessar o índice de uma lista dentro de outra lista? ou uma tupla dentro de lista ou vice-versa, exemplo:

# print(salas[1]) # Nesse caso eu acessei o ÍNDICE 1, que seria a lista ["Elaine"], mas e se dentro da lista eu quisesse acessar o valor?
# print(salas[1][0]) # Dessa forma eu entrei dentro do ÍNDICE 1 (Lista Elaine ), e estou acessando o índice 0 ("Elaine")

# # Buscando o valor Helena:
# print(salas[0][1])

# # Buscando o valor Eduarda:
# print(salas[2][2])

# #Buscando o valor 20 dentro da tupla
# print(salas[2][3][2])

for sala in salas:
    print(f" A sala é {sala}")
    for aluno in sala:
        print(aluno)
    