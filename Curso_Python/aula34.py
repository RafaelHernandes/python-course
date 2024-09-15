"""
Repetições 
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop infinito -> Quando um código não tem fim
"""
# Exemplode loop infinito:

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")
    print(f"Seu nome é: {nome}")

# Para parar um laço é possível utilizar o "break"
# Só vai sair do loop, se o usuario digitar sair, pois a condição do if vai ser verdadeira e quando
# o código ler o break ele para instantaneamente o laço de repetição.

    if nome == "sair":
        break

print ("Acabou")
    