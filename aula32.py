"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#1- Exercício
print("-----------------------------------------------------")
print("Exercicio 1")

numero_str = input("Digite um número inteiro: ")


if numero_str.isdigit():
    # O método .isdigit é para verificar se o que foi digitado é somente NÚMERO e NADA MAIS
    numero_inteiro = int(numero_str)
    par_impar = numero_inteiro % 2 == 0
    if par_impar:
        print(f"Seu número {numero_inteiro} é par! ")
    else:
        print(f"Seu número {numero_inteiro} é impar")
    
    
else:
    print("Isso não é um número inteiro")

print("-----------------------------------------------------")
print("Exercicio 2")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#2- Exercício


horario_str = input("Digite que horas são agora: ")
horario_int = int(horario_str)

horario_dia = horario_int >= 0 and horario_int <= 11
horario_tarde = horario_int >= 12 and horario_int <= 17
horario_noite = horario_int >= 18 and horario_int <= 23

if horario_dia:
    print("Bom dia!")
elif horario_tarde:
    print("Boa tarde!")
elif horario_noite:
    print("Boa noite")
else:
    print("Esse horário não existe!")
    


print("-------------------------------------------------------")
print("Exercicio 3")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#3- Exercício

nome = input("Digite o seu nome: ")

contagem_nome = len(nome)

nome_curto = contagem_nome <= 4
nome_normal = contagem_nome >= 5 and contagem_nome <= 6
nome_longo = contagem_nome > 6
if nome_curto:
    print("Seu nome é curto:")
elif nome_normal:
    print("Seu nome é normal")
elif nome_longo:
    print("Seu nome é muito grande")
print("---------------------------------------------------")