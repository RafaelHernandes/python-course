"""
While/else
"""
# Apesar de não ser muito usado, existe o While else, não é muito recomendado.

string = "Valor qualquer"
i = 0
exibir = ""

while i < len(string):
    letra = string[i]
    exibir += letra # Incremento da variável letra, antes do indice incrementar, dessa forma a variável exibir vai guardar letra pro letra 
    #print(exibir) # o Print do lado de dentro vai printar cada letra sendo somada
    i += 1
else:
    print("O else foi executado")
print("Fora do while")