"""
Formatação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = "ABC"
print(f"{variavel}")

# Supondo que eu queria preencher 10 caracteres a ESQUERDA da minha variável com algum determinado valor
# Eu faço da seguinte forma:
print(f"{variavel: >10}") # Nesse caso ele pegou o espaço e preencheu com 10 espaços
print(f"{variavel: <10}") # Nesse caso ele pegou o espaço e preencheu com 10 espaços a direita
print(f"{variavel: ^10}") # Nesse caso ele pegou o espaço e alinhou no centro com 10 espaços, porém
                    # como nossa variável tem um número ímpar de caracteres ele não vai alinhar perfeitamente
                    
# Exemplo com caracteres visiveis:

print(f"{variavel:->10}")
print(f"{variavel:-<10}")
print(f"{variavel:-^10}")

# Formatação de números:
print(f"{1000.12312312312:,.1f}") # Ele vai acrescentar 1 virgula após o primeiro valor e vai pegar 1 número
# após o ponto.

# Formatação Hexadecimal:
print(f"O hexa decimal de 1500 é {1500:X}")

                          