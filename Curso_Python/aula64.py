"""
Operação ternária (condicional de uma linha)

<valor> if <condicao> else <outro valor> <- estrutura

Basicamente seria um if e else em uma linha
"""
condicao = 10 == 10
variavel = "Valor" if condicao else "Outro valor"
print(variavel)

condicao = 10 == 11
variavel = "Valor" if condicao else "Outro valor"
print(variavel)

condicao = 15
variavel = "Valor 15" if condicao <= 15 else "Valor maior"
print(variavel)

condicao = 16
variavel = "Valor 15" if condicao <= 15 else "Valor maior"
print(variavel)