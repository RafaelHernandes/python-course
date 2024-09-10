# Sets - Conjuntos em Python - Parte 4

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # apenas valores sem ser repetidos "|"
print(s3) 
print()

s3 = s1 & s2 # Retorna somente os valores repetidos entre ambos "&"
print(s3) 
print()


s3 = s1 - s2 # Retorna o único valor da variável a esquerda "s1" que não se repete na direita, no caso o valor "1", OBS: ELE NÃO LEVA EM CONSIDERAÇÃO O 4 do s2 porque
# o s2 é a variável da DIREITA.
print(s3)
print()

s3 = s1 ^ s2 # Retorna os valores que não se repetem em ambos, valores "1" e "4"
print(s3)