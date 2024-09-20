# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
   intervalo = min(len(lista1), len(lista2)) # qual das duas lias é a menor de acordo com seu tamanho
   return [
        (lista1 [i], lista2[i]) for i in range(intervalo)
    ]
    
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))
print()
# PORÉM PODEMOS UTILIZAR DE UMA FUNÇÃO DO PYTHON QUE FAZ ISSO AUTOMATICAMENTE, exemplo:

print(list(zip(l1, l2))) # Utilizamos a list porque o zip retorna um iterator, e para consumir esse iterator exibimos em uma lista.