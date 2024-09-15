
p1 = {
    
    "nome": "Rafael",
    "sobrenome": "Ricardo Hernandes",
    "idade" : 21,
    
}

# ----------------------------------------------------- Método get

print(p1["nome"]) # Se eu tentar exibir a KEY "nome" e ela não existir, vai retornar um erro e o código vai parar.

print(p1.get("nome")) # Porém, o método get vai fazer a mesma coisa, você nao precisa das [] para buscar e se não exister a KEY que vc digitar, ele por padrão apenas retorna none
# é possível aterar a mensagem dele também, exemplo: ( para o exemplo funcionar precisa comentar a chave "nome" e o primeiro print)

print(p1.get("nome", "Não existe"))

# ------------------------------------------------------ Método POP

print() # para pular linha
nome = p1.pop("nome") # Ele atribuiu a variável nome, o conteúdo da KEY nome e depois disso deletou a chave nome
print(nome)
print(p1)
print() # para pular linha

ultima_chave = p1.popitem() # ele deleta SEMPRE a ultima chave do dicionario
print(ultima_chave) 
print(p1)
print() # para pular linha

# -------------------------------------------------------- Método update

# 1º método se usar o UPDATE

p1.update({ # Além de atualizar KEYS, ele também permite criar uma KEY nova, como por exemplo o endereço
    
    "nome": "Novo Rafael",
    "endereço": "rua xxx",
    
})

# 2º método

# p1.update(nome= "Novo Rafael", endereço = "rua xxx")


# 3º pode receber um iterável que se comporta como um dicionario como tuplas e listas.