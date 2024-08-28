"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#1- Exercício

numero_str = input("Digite um número inteiro: ")


if numero_str.isdigit():
    # O método .isdigit é para verificar se o que foi digitado é somente NÚMERO e NADA MAIS
    numero_inteiro = int(numero_str)
    if numero_inteiro % 2 == 0:
        print("Seu número é par! ")
    else:
        print("Seu número é impar")
    
    
else:
    print("Isso não é um número inteiro")

print("-----------------------------------------------------")
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#2- Exercício

horario = input("Digete que horas são agora: ")




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#3- Exercício

