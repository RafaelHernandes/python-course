# Operadores in (está entre) e not in (não está entre)
# Strings são iteráveis - possibiltando navegar entre cada letra de acordo com índices
#  0 1 2 3 4 5
#  R a f a e l
# -6-5-4-3-2-1

# Exemplo de String iterável = Acessamos com indice nome_da_variavel[x]
# Lembrando que na programação o primeiro valor sempre é 0

nome =  "Rafael" # como acessar a letra F do nome "Rafael"? com o índice abaixo, exemplo:
print(nome[2])

# Exemplo de operador IN

print("f" in nome) # Se a letra "f" está contida na variável nome, ele retorna True
print("j" in nome) # Exemplo errado, que a letra "j" NAO ESTÁ CONTIDA na variável nome, retorna False

# Esse operador não fica restrito somente a um valor, ou letra, exemplo:

print("Raf" in nome) # Verifica se "Raf" está contido na variável nome
print("Joao" in nome) # Exemplo errado para retornar o False.