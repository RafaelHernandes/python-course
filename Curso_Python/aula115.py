import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos = copy.deepcopy(produtos) # Realizando a cópia dos produtos originais, nunca manipule os dados originais diretamente.

def exibir(produtos):
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
    print()

    
for produto in novos_produtos:
    produto["preco"] *= 1.10 # Aumentando em 10% os valores 
    produto["preco"] = round(produto["preco"], 2) # arredondando para duas casas decimais
       

print("Produtos com acréscimo de 10%")
print()
print(*novos_produtos, sep="\n")
print()



# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

on = sorted(novos_produtos, key=lambda item: item["nome"], reverse= True)
produtos_ordenados_por_nome = copy.deepcopy(on)
print("Produtos ordenados por nome: ")
exibir(produtos_ordenados_por_nome)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
op = sorted(novos_produtos, key=lambda item: item["preco"])
produtos_ordenados_por_preco = copy.deepcopy(op)
print("Produtos ordenados por preco: ")
exibir(produtos_ordenados_por_preco)

