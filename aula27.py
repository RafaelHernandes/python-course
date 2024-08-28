"""
Fatiamento de strings


Fatiamento [i:f:p] [::]

i = inicio
f = fim
p = passo

Obs: a função len retorna a quantidade de caracteres da string
"""
# Você pode definir aonde comecar o fatiamento, o fatiamento nada mais é do que você definir um índice,
# De onde ele vai começar a exibir a sua variável, por exemplo se eu colocar variavel[4] ele vai pegar o quarto índice
# e vai exibir, lembre-se que o índice começa em 0, então ele vai exibir a letra "m" no caso da variável "Olá mundo"
# agora para eu exibir do m para frente, eu posso definir como variavel[4:8], esse fatiamento sempre precisa ser 1 valor a mais
# do que o índice que deseja, caso você queira que pare na letra "n" precisa definir 7, pois o "n" está na posição 6
# e como foi dito antes, é necessario colocar 1 valor a mais sempre, pra atingir a posição que vc deseja.

variavel = "Olá mundo"

print(variavel[4])
print(variavel[4:7]) # Defini inicio do primeiro parâmetro 4, e vai até o 7

# E caso você queira que ele vá até o final da string, escrevendo do primeiro parâmetro até o fim, apenas omitir o dado funciona
# exemplo:

print(variavel[4:]) # Defini o inicio do 4 índice, omiti o ultimo ele vai até o final

# E também é possível realizar inversamente, exemplo:

print(variavel[0:5]) # Defini para inicio do indice 0 até o 5
print(variavel[:5]) # Omiti o primeiro parâmetro, ele começa do 0 e vai até o 5


# É possível fazer com índices negativos, aonde você declara negativo e ele leva em considerao o ultimo e depois o primeiro, exemplo:

print(variavel[-9:-2]) # 9 é meu ultimo índice, nesse caso seria equivalente a 0, -2 seria equiavelnte a 7

# Função len, conta a quantidade de caracteres, exemplo:

print(len(variavel)) # 9 pois o espaço está incluído como caractere

# Obs, a contagem é diferente do índice, a contagem começa do 1, o índice do 0

# Exemplo com i : f : p

print(variavel[0:9:1]) # Inicia do 0, vai até o índice 9 (ultimo índice) e vai passar de 1 em 1


# Exemplo dele coletando os índices a cada 2 casas

print(variavel[0:9:2]) # Inicia do 0, vai até o índice 9 (ultimo índice) e vai passar de 2 em 2

# E também é possível usar indices negativos no passo, exemplo:

print(variavel [::-1]) # nesse caso ele vai começar do primeiro valor, vai pegar todas as casas e vai até o final