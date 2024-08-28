"""
Exercicio:

Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    exiba:
    
        seu nome é {nome}
        seu nome invertido é {}
        se nome contém (ou nao) espaços
        seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
        
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome and idade:  # Jeito do professor
# if nome and idade != False: - Meu jeito, que está dando errado quando o Nome é preenchido e a idade não, ele NAO retorna o else.
    print(f"Seu nome é {nome} ")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome tem espaços! ")
    else:
        print("Seu nome não tem espaços ")
    print(f"Seu nome tem {len(nome)} letras ")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A ultima letra do seu nome é '{nome[-1]}'")
else:
    print("Desculpe você deixou campos vazios.")