"""
Retorno de valores das funções (return)

"""

# Existem funções que só executam ações, como por exemplo print(), e não retornam nenhum valor pois não precisamos do valor que o print retorna

# E existem funções que podem executar e retornar valores.

def soma(x,  y):
    if x > 10:
        return [10, 20] # Código para aqui e não exibe mais nada após o primeiro return lido, ou seja, só é possível um return
    
    return x + y # Utilizar o return significa que vai retornar algo e que esse valor vai ficar utilizavél para ser atribuido com variáveis ou algo do tipo
    # return sómente é utilizado de dentro das funções
    
    print("TESTE") # O Python não executada nada que está alem do return em uma função

# Só tem 1 return por função, pois nada além do return é executado.

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma(11, 55))