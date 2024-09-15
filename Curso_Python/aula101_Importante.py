# Generator expression, Iterables e Iterators em Python

# Iterable =  tem a responsabilidade de ter todos os valores sequêncialmente

# Iterator = Te entrega um valor por vez, no caso qual que é o próximo valor, ele não sabe quem é o anterior, o primeiro ou o ultimo, não é possível acessar indice de iterator
# Não é possível acessar len() do iterator, next() etc..

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable) # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))
# caso você print além do que há iteradores ele retorna um erro
print(next(iterator))

# Curiosidade: O Iterator esgota os valores, quando você está fazendo um laço de repetição e exibindo os próximos valores, não é possível fazer um laço dentro do outro utilizando
# o MESMO iterator, pois ele sempre vai continuar de onde parou
