# List comprehension com mais de um FOR

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))#Como estamos adicionando dois valores diferentes na lista, foi necessário criar uma TUPLA (x, y) pois não é possível colocar 2 valores em 1 índice

lista = [
    (x, y) # Lado esquerdo, utilizado para mapeamento, o que vai ser inserido na lista nova
    for x in range(3)
    for y in range(3)   
]

print(lista)

# Para mais dúvidas sobre list comprehension https://youtu.be/1YbTDczvqco