import sys

#Genetor expression, Iterables e Iterators em Python

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable) # tem __iter__ e __next__

# Todo genereator também é um Iterator, mas um Iterator NÃO É um generator

# Generator é uma função que pausa em determinado local e executa algo.

generator = ( # Generator expression
    
    n for n in range(10000)
)
lista = [ # list comprehension
    
    n for n in range(10000)
]

print(sys.getsizeof(generator)) # nesse caso ele está mostrando sempre o valor do PRIMEIRO VALOR pois ele está pausado na primeira execuçãO
print(sys.getsizeof(lista)) # Já a lista está armazenando 10000 números, e está guardando tudo na memória, e posso acessar QUALQUER VALOR DA LISTA