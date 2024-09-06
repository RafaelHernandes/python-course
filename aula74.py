"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos

Retorne o total para uma variável e mostre o valor da variável.

Crie uma função fala se um número é par ou ímpar. 

Retorne se o número é par ou impar

"""
def multiplicacao(*args):
    total = 1 # índice para multiplicar valores

    for numero in args: # desempacotou
        
        if numero == 0: # para caso o valor seja 0, ele não dar problema e zerar a multiplicação
            total = total + numero 
        else:
            total = total * numero #  multiplicando
    return total


def parOuImpar(x):
    if x % 2 == 0:
        return f"O número {x} é par!"
    # NÃO É NECESSÁRIO USAR ELSE, POIS QUANDO LER O ELSE ELE NÃO LÊ NADA A MAIS, o que torna o else REDUNDANTE, pois se o número não for par, ele só pode ser ímpar.
    return f"O numero {x} é ímpar!"

print(parOuImpar(2))
print(multiplicacao(1,2,3,0,2))
