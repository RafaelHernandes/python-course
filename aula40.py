"""
Calculadora com While
"""

# 1º Passo, criar os inputs solicitando os números e o operador, e as variáveis que posteriormente vao converter para float
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None # Criado a variável de flag para validação
    num_1_float = 0
    num_2_float = 0
# ---------------------------------------------#
   

# 2º Passo, criar um try, except para validar e converter os números que estão como string para float, no caso se digitarem letras, o float não vai converter e invés de dar erro
# e não funcionar mais o código, ele apenas vai pegar esse erro e ir para o except, aonde vai manter a Flag criada com valor None, dito isso ele vai cair no primeiro IF e 
# recomeçar o programa
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True # Flag de validação
    except:
        numeros_validos = None # Flag de validação
#------------------------------------------------#

# 3º Passo, validar se o valor de numeros_validos está como None, significa que ele NÃO PASSOU na conversão do TRY e os números não foram convertidos
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue # Para o código nesse exato momento e retorna ao inicio.
#------------------------------------------------#

# 4º Passo, criar uma variável para comparar o tipo de operador digitado, com os tipos permitidos
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos: # Caso o valor digitado na variável operador NÃO ESTEJA CONTIDO dentro da variável operadores_permitidos, vai retornar ao começo.
        print('Operador inválido.')
        continue # Para o código nesse exato momento e retorna ao inicio.
#------------------------------------------------#

# 5º Passo, verificar se o número de operadores foi maior que 1, nesse caso também irá retornar para o início do código
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue # Para o código nesse exato momento e retorna ao inicio.
#------------------------------------------------#

# 6º Passo, os as contas/variáveis de cada operador.

    operador_mais = num_1_float + num_2_float
    operador_menos = num_1_float - num_2_float
    operador_vezes = num_1_float * num_2_float
    operador_divisao = num_1_float / num_2_float
#------------------------------------------------#

# 7º Passo, validar qual operador que foi digitado para escolher a conta correta

    # Conta de adição
    if operador == "+":
        print(operador_mais)
        
    # Conta de divisão
    elif operador == "-":
        print(operador_menos)
        
    # Conta de multiplicação
    elif operador == "*":
        print(operador_vezes)
    else:
        print(operador_divisao)
# -----------------------------------------------#


#  8 Passo, opção de sair da calculadora, ou não
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
        
    