# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
print_iter(combinations(pessoas, 2)) # Ele gera todas as possíveis combinações de acordo com os elementos em pessoas, em pares (2), obs: sem repetições
print_iter(permutations(pessoas, 2)) # A diferença para o combinations é q ele repete, exemplo: João e joana, joana e joão.
print_iter(product(*camisetas)) # Faz a combinação de todos os tipos de elementos possíveis.