# Operadores aritméticos

adicao = 10 + 10
print("Adição", adicao)

subtracao = 10 -5
print("Subtração", subtracao)

multiplicacao = 10 * 10
print("Multiplicação", multiplicacao)

divisao = 10 / 2.2 # Sempre retorna float, independente se o resultado for inteiro ou não.
print("Divisão", divisao)

divisao_inteira = 10 // 2.2 # Todos os valores após o ponto no caso de uma divisão com float, será zerado.
# e se for um número inteiro divisivel, retorna sem ser float, exemplo: 10 / 2 = 5
print("Divisão inteira", divisao_inteira)

exponenciacao = 2 ** 10 # Nesse caso o primeiro valor é o que está sendo elevado ao segundo, no caso 2 elevado a 10.
print("Exponenciação", exponenciacao)

modulo = 55 % 2 #resto da divisão
print("Módulo", modulo)

# Para que serve o resto da divisão? por exemplo para exercícios aonde pede para saber se o número é par ou impar
# Se o RESTO DA DIVISÃO (Módulo) der 0, então é par, se não der 0 então ele é impar.

