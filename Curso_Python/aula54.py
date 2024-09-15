# EXERCÍCIO PARA CONTAR OS ÍNDICES DA LISTA E EXIBIR ELES

lista = ["Rafael", "Bianca", "João"]
indices = range(len(lista)) # o range vai contar quantos itens tem no len(lista), pois se eu chamasse somente o len(lista) ele iria contar cada caractere entre as aspas separadas
# por vírgulas, então range vai contar como apenas 1 único item entre as vírgulas

for indice in indices:
    print(indice, lista[indice]) # Exibindo o indice e a lista de acordo com cada índice
