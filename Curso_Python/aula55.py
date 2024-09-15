"""
Introdução ao desempacotamento + tuples (tuplas)
"""
nomes = ["Rafael", "Bianca", "João"] # lista

# Desempacotamento, seria extrair os valores de uma lista e transforma-los em variáveis, é bem simples, exemplo:

nome1, nome2, nome3 = nomes # sempre declare a quantidade de variáveis de acordo com a quantidade de elementos na lista

print(nome1)
print(nome2)
print(nome3)

# Também é possível fazer da seguinte forma, exemplo:

nome4, nome5, nome6 = ["Vanessa", "André", "Gabriel"] # Funciona da mesma forma como está lá em cima

# E no caso de você ter menos variáveis e mais valores e quiser acessar os valores que não foram declarados como os exemplos acima, exemplo:

# nome7, nome8 = ["Diego", "Nathan", "Eduardo"] # Como acessar o Eduardo se não foi declarada uma terceira variável, você declara uma variável para englobar o resto dos dados que
# você não quer acessar, exemplo:

nome7, *resto = ["Diego", "Nathan", "Eduardo"]
print(nome7) # Mostrou somente o primeiro valor "Diego" e a variávell *resto empacotou os demais valores, mas também é possível visualizar a variável resto, exemplo:
print(nome7, resto) # Ele criou uma lista a parte com o resto da primeira lista como foi pedido

# E o caso de você querer acessar o valor que está no meio, no caso o nome Nathan, é só fazer da seguinte forma, declarar o resto antes e depois do nome, exemplo:


resto, nome7, *resto = ["Diego", "Nathan", "Eduardo"]
print(nome7)

# E para acessar o terceiro valor:

resto, resto, nome7, *resto = ["Diego", "Nathan", "Eduardo"]
print(nome7)