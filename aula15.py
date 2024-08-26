# Funcão para coletar dados (digitar dados na tela)

# nome = input("Qual o seu nome? ")
# print(f"O seu nome é {nome}")
 

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
# print(f"A soma dos números é: {numero_1 + numero_2}")

# É possível fazer a coersão antes do input mas não é uma boa prática pois futuramente pode dar problema
# exemplo, se eu digitar a letra "A" não vai ter como a coersão ser feita e o programa vai quebrar antes
# do programador ter a possibilidade de checar o que o usuario digitou.

# A boa prática seria fazer da forma abaixo, (TENDO EM VISTA QUE SERIA NECESSÁRIO UMA CHECAGEM ANTES)

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# Dessa forma é possível usar as variáveis para checar o tipo de dado que o usuario digitou antes de converter.
# Exemplo: Usando um IF para verificar se o resto da divisao do numero digitado é divisivel por 1 que 
# Retornasse 0 pois dessa forma saberiamos se é um numero.

print(f"A soma dos números é: {int_numero_1 + int_numero_2}")