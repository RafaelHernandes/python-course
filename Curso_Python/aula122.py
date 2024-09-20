# count é um iterador sem fim

from itertools import count

c1 = count() # Ele é um contador infinito

for i in c1: # Laço infinito
    if i >= 100:
        break
    i += 1
    print(i) 