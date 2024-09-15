"""
Higher Order Functions = Funções de primeira classe

O que isso quer dizer?
R: Funções que podem receber e/ou retornar outras funções

Conhecimento de aula: Funções podem ser parâmetros de outras funções
"""

def saudacao(msg, nome):
    return f"{msg}, {nome}!"

def executa(funcao, *args): # Minha função executa, recebe um parâmetro denominado de funcao e outro parâmetro do tipo *args que serve para empacotar quaisquer tipos de dados                  
    return funcao(*args)
    
v = executa(saudacao, "Bom dia", "Rafael Ricardo") # nesse caso a função "executa" foi dada a ela que seu primeiro valor é outra função, e os demais valores entrariam no *args
print(v)

