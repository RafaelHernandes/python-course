# Manipulando chaves e valores em dicionários

pessoa = {} # Criando um dicionario vazio aonde vai ser adicionado dados depois
##
##
teste = input("Digite seu nome: ")

pessoa["nome"] = teste # Chamamos a lista pessoa, abrimos colchetes e declaramos e criamos uma chave chamada de nome, aonde ele recebe o input de dados "teste"

print(pessoa["nome"])
print() # Para pular espaço

# Exemplo de chave dinâmica

chave = "altura"
pessoa[chave] = 1.85
print(pessoa[chave])
print() # para pular espaço

chave2 = "dado_para_apagar"
pessoa[chave2] = "laranja"
del pessoa[chave2] # Deletei a chave2 do dicionario pessoa
print(pessoa)
# Porque criar chave dinâmica? pois se você quiser alterar o nome da chave sem gerar erros, agora você pode