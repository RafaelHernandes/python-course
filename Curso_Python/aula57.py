"""
enumerate - enumera iteráveis (índices)

"""
# Afinail o que é o enumerate? ele basicamente cria um TUPLA com sua lista e adiciona um índice

lista = ["Rafael", "João", "Maria"]
lista.append("Vinicius")

# lista_enumerada = enumerate(lista) # o Enumarate vai numerar cada um dos itens da lista

# Sempre que é usado o enumerate, não é prudente atribuir ele a uma variável pois depois que ele é utilizado a primeira vez ele não realiza mais sua função, exemplo:

# Invés de eu passar for item in lista_enumerada, eu passo direto o enumerate(lista), dessa forma posso realizar mais "for"
for item in enumerate(lista):     #Exibe cada um dos itens da lista e seus respectivos índices
    print(item) 

# Mas nesse caso a tupla é um dado imutável, como realizamos o desempacotamento aqui? simples, apenas declarando o indice e o nome, exemplo:

for indice, nome in enumerate(lista):
    print(indice,nome)
    
# A unica diferença foi que declarei uma variável para o indice e outra para o nome
