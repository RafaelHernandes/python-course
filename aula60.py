"""
Split e Join com list e str

split - divide uma string

join - une uma string

"""

frase = "Olha só que, coisa interessante"

lista_palavras = frase.split()
print(lista_palavras)

# Também permite definir em qual momento/caractere ele vai realizar a quebra de palavras, exemplo:

lista_palavras = frase.split(",") # Dividiu a frase e quebrou ela na vírgula
print(lista_palavras)

# Basicamente você definir algo dentro do split, significa q ele vai cortar algo que esteja sendo definido dentro do ()

# É possível refirnar mais ainda essa lista, utilizando o método FOR, exemplo:

for indice, frase in enumerate(lista_palavras):
    print(lista_palavras[indice].strip()) # Porque passar o indice como parâmetro? pois no momento em que foi dividido no meio a frase, gerou 2 str e 2 índices, porém 
    # sabemos que str é imutável, então passamos o índice.
    # o método STRIP faz nada mais e nada menos do que remover os espaços do começo e do fim 
    
for indice, frase in enumerate(lista_palavras):
    print(lista_palavras[indice].rstrip()) # o rstrip corta somente o espaço do lado direito
    
for indice, frase in enumerate(lista_palavras):
    print(lista_palavras[indice].lstrip()) # o lstrip corta somente o espaço do lado esquerdo
    

# UTILIZAÇÃO DO JOIN

frases_unidas = ",".join(lista_palavras) # Diferente do split, eu passo dentro do parâmetro o que eu quero unir, no caso o separador.
# dentro de "" eu passei qual era o separador, e no .join() eu passei qual era a variável a ser unida, e o join só aceita ITERAVEIS, no caso não aceitaria números
print(frases_unidas)