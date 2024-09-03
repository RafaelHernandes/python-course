import os # import para limpar o terminal
opcoes_validas = "ial"
lista = []


while True:
    opcao = input("Selecione uma opção\n"
                    "[i]nserir [a]pagar [l]istar: ")
    os.system("cls") # limpa o terminal

    if opcao not in opcoes_validas:
        print("Digite uma opção válida!")
        continue
    
    if opcao == "i":
        valor = input("Digite o valor a ser inserido: ")
        lista.append(valor)        
        
    if opcao == "a":
        indice_str = input("Digite o índice a ser excluído: ")
        
    
        if not indice_str.isdigit():
            print("Esse índice não existe!")
            continue
        else:
            indice_int = int(indice_str)
            del lista[indice_int]
            continue
        
    if opcao == "l":
        if  len(lista) == 0:
            print("A lista está vazia!")
            
        for indice2, nome in enumerate(lista):
            print(indice2, nome)
            continue
    
    
    
    
            
    
    
    
            

