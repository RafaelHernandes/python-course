# Shallow Copy vs Deep Copy em dados mutáveis

# Shallow Copy =  Copia rasa
# Deep Copy = Copia profunda

import copy # Necessário para usar o Deep Copy

dicionario1 = {
    'chave1': 1,
    'chave2': 2,
    'chave3': 3,
}


# Apesar de eu falar que dicionario2 é igual a dicionario1, ao usar o método .copy() ele me permitiu apenas apenas alterar o dicionario2 por que são valores imutáveis, no caso de 
# Haver valores mutáveis, ele vai apenas vai fazer ambas variáveis apontarem para a mesma coisa na memória, exemplo:

dicionario1["lista1"] = [0, 1, 2] # Agora que há um valor mutável aqui dentro, tanto dicionario1 quando dicionario2 apontam para a mesma lista apesar do .copy(), que é considerado
# um shallow copy, (copia rasa)

dicionario2 = dicionario1.copy()

dicionario2['chave1'] = 1000
dicionario2["lista1"][1] = 9999 # agora ambos foram alterados pois nesse caso a lista é um dado mutável, o que torna o .copy() uma cópia rasa.
print(dicionario1)
print(dicionario2)

# Ao utilizar o deep copy, podemos visualizar que um dificionario não afeta o outro, exemplo:

print()
dicionario3 = {
    'chave1': 1,
    'chave2': 2,
    'chave3': 3,
    'lista1': [100, 200, 300]
}

dicionario3["lista1"] = [4, 5, 6]

dicionario4 = copy.deepcopy(dicionario3)

dicionario4["chave1"] = 150
dicionario4["lista1"][1] = 100000

print(dicionario3)
print(dicionario4) # Agora visualizamos que um dicionario não afeta o outro em relação a dados mutáveis
