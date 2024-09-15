"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "batata"
tentativas = 0
letras_acertadas = ""

while True:
    
    
    letra = input("Digite uma letra: ")
    tentativas += 1
    
    if len(letra) > 1: 
        print("Digite apenas UMA letra!")
        continue
    
    if letra in palavra_secreta:
       letras_acertadas += letra

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
            
        else:
            palavra_formada += "*"
    
    print(palavra_formada)
    
    if letra not in palavra_secreta:
        print("Letra não contida na palavra secreta, digite outra")
        continue
        
    if palavra_formada == palavra_secreta:
        os.system("cls") # utilizado o Import os para dar clear automaticamente após passar de um ponto o código
        print(f"VOCÊ GANHOU PARABÉNS!!!")
        print(f"Numero de tentativas: {tentativas}")
        palavra_secreta = "batata"
        tentativas = 0
        letras_acertadas = ""
        