frase = "ValooooooOr qualquer" # Colocado diversas letras "a" propositalmente para o entendimento da lógica do código
i = 0 #indice de repetição do while
contador = 0 # contador de letras
letra_mais_frequente = "" # variável que vai armazenar a letra que mais aparece

while i < len(frase): # se o i for menor que o tamanho da frase...
    letra_atual = frase[i] # atribui a variável letra_atual a quantidade de letras da frase
    contagem_letras = frase.lower().count(letra_atual.lower()) # contagem_letras está recebendo a variavel frase com todas as letras minúsculas e contando.
    
    if contador < contagem_letras and letra_atual != " ": # Se o contador for menor que a contagem_letras e letra_atual diferente de vazio...
        contador = contagem_letras
        letra_mais_frequente = letra_atual
        
    i += 1

print(f"Letra: {letra_mais_frequente} apareceu {contador} vezes.")
