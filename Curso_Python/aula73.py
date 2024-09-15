"""
args - Argumentos não nomeados

* -args(empacotamento e desempacotamento)

Lembre-te de desempacotamento
"""

x, y, *resto = 1, 2, 3, 4 # Tupla

print(x, y, resto) # x e y(1 e 2) desempacotado e *resto está empacotado ( 3 e 4)

def soma(x, y):
    return x + y

def soma(*args): # Somente argumentos não nomeados
    total = 0
    # Como somar uma tupla?
    for numero in args: # desempacotou
        total = total + numero # somando cada valor ao total
    return total
    
    
# print(sum(1,2,3,4,6,7,8)) - dessa forma vai gerar um erro dizendo que está recebendo mais do que dois argumentos, como resolver isso?

numeros = 1, 2, 3, 4, 6, 7, 8
exemplo = soma(*numeros) # Ao declarar os valores inteiros na variavel numeros, mandei ele realizar a soma desempacotando os valores, ou seja, os valores não serão uma tupla
print(exemplo)
# Agora podemos usar a função sum da forma correta.

print(sum(numeros))
