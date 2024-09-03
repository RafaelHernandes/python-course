"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754

"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(f"{numero_3:.2f}") # Primeira forma de contornar o erro de precisão dos floats, porém nesse caso a gente retorna uma string, porquê utilizamos a formatação f

print(round(numero_3, 3)) # Segunda forma, utilizando a função round, ela basicamente funciona aonde vc declara sua variável e quantos valores vc quer após o ponto flutuante
# porém se os valores após o ponto flutuante forem 0 ela nao vai exibir.

# A terceira forma é utilizando o decimal, é necessário importar e ao declarar fica da seguinte forma:

numero_4 = decimal.Decimal(0.5)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5
# Mas o correto é passar um valor em string dentro dessa função .Decimal() e não um float, e vai fazer toda a lógica de conversão da string
print(numero_6)

# Passando o valor em String, a primeira conta ja sai como correta, exemplo:

numero_7 = decimal.Decimal("0.5")
numero_8 = decimal.Decimal("0.7")
numero_9 = numero_7 + numero_8

print(numero_9)

# E isso também torna a função round utilizável do jeito correto, apresentando a segunda casa, exemplo:
print(round(numero_9,2))

