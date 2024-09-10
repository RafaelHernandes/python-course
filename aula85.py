# Sets - Conjuntos em Python - Parte 2

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {1, 2, 3, 3, 3, 3, 3, 3, 1}
print(s1) # Elimina valores duplicados por conta própria
print()
# Muito utilizado para fazer remoção de dados duplicados em listas, tuplas, etc.. exemplo:

l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
print(l1) # Vendo os dados da lista antes da remoção dos dados duplicados
print()
s2 = set(l1) # Transformei minha lista em um SET, assim ele ja vai remover todos os dados duplicados
l2 = list(s2) # Transformando meu SET em lista novamente
print(l2)
