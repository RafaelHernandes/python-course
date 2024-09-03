"""
For + Range 

range -> range(start, stop, step)
"""
# Se eu passar um único parâmetro, ele vai entender que foi um STOP, aonde eu quero que pare, o start vai ser 0  e o step vai ser 1
numeros = range(10)

# Se eu passar o Start e o Stop, o STEP vai continuar sendo um, e dessa vez você define de qual valor o RANGE começa, exemplo:
numeros2 = range(5,10)

# Se eu quiser um range que começa de 5, vai até 10 e PULA de 2 em 2 números, então seguimos conforme o range abaixo
numeros3 = range(5,10,2)

print(numeros)
print(numeros2)
print(numeros3)

# E como exibir esses valores? precisamos utilizar o for para isso.
# Curiosidade do FOR: não precisamos declarar um indice de autoincremento para que o FOR funcione, pois ele já faz isso automaticamente.


for valor in numeros: # PARA cada VALOR CONTIDO EM NUMEROS, faça:
    print(valor)
    # Apenas foi definido a variável "valor" que recebeu o range "numeros" e armazenou todos os seus valores e exibiu, sem necessidade de indice
    
    