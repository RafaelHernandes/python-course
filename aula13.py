# Formatação de Strings com o exercício de IMC

# f-strings 


nome = "Rafael Ricardo Hernandes"
altura = 1.85
peso = 86
imc = peso / (altura * altura)

# print(nome, "tem", altura, "pesa", peso, "quilos, e seu imc é:")
# print(imc)

# Como exibir tudo do primeiro print em uma única VARIÁVEL:

linha_1 = "nome, tem, altura, pesa, peso, quilos, e seu imc é:"

# Ao inserir o caractere "f" antes do texto, ele já reconhece e permite usar variáveis dentro daquele texto, 
# utilizando as {} nas variáveis, exemplo:

linha_1 = f"{nome} tem {altura} de altura pesa {peso} quilos e seu imc é {imc}"
print(linha_1)

# E também permite formatar a quantidade de casas de um número utilizando o ":." e o "valor de casas" e o caractere "f", exemplo:

linha_1 = f"{nome} tem {altura} de altura pesa {peso} quilos e seu imc é {imc:.3f}"
print(linha_1)
