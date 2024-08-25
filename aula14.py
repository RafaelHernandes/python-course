# Formatação de strings com o método format

a = "A"

b = "B"

c = 1.1

string =  "a= {} b= {} c= {}" 
formato = string.format(a, b, c)
# Ao utilizar o método format, deve-se escrever a mensagem e declarar dentro de {} de acordo com a ordem exibida no .format

#caso você tente inserir um número maior de "{}" do que de elementos dentro do .format, VAI DAR ERRO, exemplo:

#formato = "a= {} b= {} c= {} d= {}".format(a, b, c)

# Ou como todas as coisas que tem índice em programação começam com 0, você declara o valor da posição, exemplo:

string =  "a= {0} a= {0} a= {0} b= {1} c= {2}" 
formato = string.format(a, b, c)

# dessa forma não importa se você excedeu mais {} do que  numero de quantidade no .format, pois você só está exibindo novamente
# o mesmo valor
print(formato)

