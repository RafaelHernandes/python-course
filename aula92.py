# Empacotamento e desempacotamento de dicionários.

pessoa = {
    "nome": "Rafael",
    "Sobrenome": "Ricardo Hernandes",
}

a, b = pessoa.values() # Sem o . values() ele retorna somente as chaves, com o , values() ele retorna os valores
print(a, b)
print()
# Para desempacotar a chave e o valor:
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) # Pegou a primeira chave e o primeiro valor
print(b1, b2) # pegou a segunda chave e os segundo valor
print()
dados_pessoa = {
    "idade": 21,
    "altura": 1.85,
}

pessoa_completa = {
    **pessoa, **dados_pessoa # Extraindo dicionarios e juntando em um único ao utilizar "**" e o nome do dicionario
}
print(pessoa_completa)

# args e kwargs
# kwargs - Keyword arguments ( argumentos noemados )

def argNomeados(*args, **kwargs):
    print("Não nomeados", args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

print()
    
# argNomeados(1, 2, nome="Joana", qualquer=123) # 1 e 2 não são nomeados

# e a cereja do bolo, como desempacotar um dicionario que é nomeado?

argNomeados(**pessoa_completa)