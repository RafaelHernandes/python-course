# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

print(list(range(10)))
print()

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
print()

# Utilizando list comprehension em Python

lista = [numero for numero in range(10)] # ADICIONE A ESQUEDA DO SEU FOR O QUE VC DESEJA Q SEJA INCLUÍDO
print(lista)
print()

lista = [numero * 2 for numero in range(10)] # É possível fazer até mesmo expressões matemáticas
print(lista)