# Exercício de CPF Válido 

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

"""
import os
multiplicador_1 = 10
multiplicador_2 = 11 
resultado_final = 0 
resultado_final2 = 0 
resultado = 0
resultado2 = 0
lista_cpf = []
cpf_final = "" 
cpf_formatado = ""

while True:
    cpf = input("Digite os 9 primeiros digitos: ")
    os.system("cls")
    

# Validação 1: Se o que foi digitado eram apenas números INTEIROS
    if not cpf.isdigit():
        print("Digite apenas 9 digitos inteiros!")
        continue
    
#Validação 2: Se a quantidade de digitos passou de 9   
    elif len(cpf) > 9:
        print("Quantidade de 9 digitos excedida!")
        continue
    
    elif len(cpf) < 9:
        print("Digite exatamente 9 digitos!")
        continue
    
    lista_cpf = cpf
    
    for calculo in cpf:
        
        # Minha forma  de fazer
        
        calculo_int = int(calculo) # Transformei os digitos em inteiro para multiplicar com a contagem regressiva
        resultado = calculo_int* multiplicador_1 # Multiplico o calculo_int pelo multiplicador que começa de 10 e vai subtraindo
        resultado_final += resultado # Somo na variável resultado_final todos os valores da variável resultado
        multiplicador_1 -= 1 # Multiplicador do primeiro digito
        
    
    
    conta1 = (resultado_final *10) % 11
    
    
    if conta1 <= 9:
        print(f"Seu primeiro digito é: {conta1}")
    else:
        conta1 = 0
        print(f"Seu primeiro digito é: {conta1}")
    
    #-----Calculo segundo digito-----#
    
    lista_cpf += str(conta1)
    cpf_final += lista_cpf
    
    for calculo2 in lista_cpf:
      calculo_int2 = int(calculo2)
      resultado_2 = calculo_int2 * multiplicador_2
      resultado_final2 += resultado_2
      multiplicador_2 -= 1
        
    conta2 = (resultado_final2 * 10) % 11
    
    if conta2 <= 9:
        print(f"Seu segundo digito é: {conta2}")
        cpf_final += str(conta2)
    else:
        conta2 = 0
        print(f"Seu segundo digito é: {conta2}")
        cpf_final += str(conta2)
    

    print(f"O seu CPF válido é: {cpf_final[:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:]}")
    break