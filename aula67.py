"""
Introdução as funções (def) em Python

Funções são trechos de códigos usados para 
replicar determinada ação ao longo do seu código.

Elas podem receber valores para parâmetros(argumentos)
e retornar um valor específico.

Por padrão, funções Python retornam None (nada).
"""

def Print(): # def "nome_da_função":
    print("Varias1") # o que a função vai fazer
    print("Varias2")
    print("Varias3")
    print("Varias4")
    
# Sabemos que nenhuma função começa com letra maíscula, e não é boa prática criar uma com letra maíscula, mas somente para didática veja como funciona a definição de uma:
Print() # função Print com P maiscula criada.
# Funções são muito utilizadas para blocos de códigos que vão se repetir bastante durante um código, para isso é criado uma única vez como função e depois chamamos ela.

# Exemplo com parâmetros:

def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3) # Basicamente foi declarado 3 parâmetros dentro da função (a, b e c) e na hora de imprimir eu declarei 1 valor para cada, em ordem