# While - Parte 3 ( Continue )

contador = 0 

while contador <= 100:
    contador += 1
    # -------------------------------------#
    if contador >= 10 and contador <= 27:
        continue # Faz ignorar o contador sem que o bloco de código seja interrompido
    # Nesse caso, entre 10 e 27 ele não vai exibir na tela, mas também não vai parar o código
    
    print(contador)
    # -------------------------------------#
    if contador == 40:
        break

print("Acabou")

