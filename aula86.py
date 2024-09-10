# Sets - Conjuntos em Python - Parte 3


# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add("Rafael") # .add() só envia 1 valor por vez
s1.add(1)
#s1.update("Olá mundo") # Dessa forma ele vai mandar letra por letra, como mandar uma frase?, exemplo:
s1.update(("Olá mundo",1, 2, 3, 4))
#s1.clear() # limpa o set
s1.discard("Olá mundo") # apesar de não ter índices, ao ser imutavél, quando você passar o valor em sí, ele vai deletar.
s1.discard("Rafael")
print(s1)