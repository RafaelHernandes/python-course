"""
Interpolação básica de strings
    
s - string
    
d e i - int
    
f - float

x e X - Hexadecimal(0123456789ABCDEF)
"""
# O que é a interpolação? é básicamente a formatação de string igual format ou f-string, exemplo:
# invés de utilizar {nome_da_variável}, você coloca % e a letra que representa o tipo daquela variável.
# Após isso vc coloca um % fora do "" e abre um parenteses e declara o nome das variáveis de acordo com
# Os tipos que foram inputados e em suas respectivas ordens.

# Segue o exemplo abaixo:

nome = "Rafael"
preco = 1000.25050
variavel = "%s, o preço é R$%.2f" % (nome, preco) # %s é referante a variavel do tipo string  
                                                # e o %f a variavel do tipo float, o .2 é formatação de casas
print(variavel)

# Exemplo de hexadecimal, converti um valor inteiro (15) em 15 hexadecimal. Valores declarados na hora
print("O hexadecimal de %d é %x" % (15, 15)) 

