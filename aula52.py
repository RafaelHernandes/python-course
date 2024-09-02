"""
Cuidados com dados mutáveis
= -  copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ["Rafael", "João"]
lista_b = lista_a # Ao declarar a lista_b = lista_a significa que esses dois "nomes" apontam para a mesma variável, se alterar uma delas, a outra também é alterada 
# isso só acontece pois o que foi atribuido a lista_a é um valor MUTÁVEL, a lista é um tipo mutável.
print(lista_b)
lista_a[0] = "Qualquer coisa"
print(lista_b)

# E caso você queira copiar uma lista sem que a outra seja afetada? usando o método .copy(), exemplo:

lista_b = lista_a.copy()
lista_a.append("David")
print(lista_b)
print(lista_a) # Como podemos ver, o david está incluso na lista_a mas não na lista_b, pois agora cada uma aponta para uma diferente