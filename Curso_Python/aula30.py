"""
CONSTANTE = "Variáveis" que não vão mudar

Muitas condições no mesmo if (ruim)

    <- Contagem de complexidade (ruim)
    
Utiliza-se letra maíscula para variáveis que não vão mudar o valor, ou que não devem ser mudadas.

"""

velocidade = 60 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1 (CONSTANTE)
LOCAL_1 = 100 # local onde o radar 1 está (CONSTANTE)
RADAR_RANGE = 1 # A distância onde o radar pega (CONSTANTE)

# Simplificando as expressões, para ter menos informações no if:

velocidade_excedida = velocidade > RADAR_1 
# \ serve para quebrar linha, nesse caso para a variável carro multado, o carro precisa estar entre o local 99 e 101 e acima de 60 KM/h
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                local_carro <= (LOCAL_1 + RADAR_RANGE)


if velocidade_excedida:
    print("O carro excedeu a velocidade do radar 1: ")
    
    if carro_multado:
        print(" O carro foi multado ")
    else:
        print("O carro não foi multado ")
else:
    print("O carro estava dentro da velocidade permitida.")
    

# Exemplo de como estava antes:

# if velocidade > RADAR_1:
#     print("O carro excedeu a velocidade do radar 1: ")
    
#     if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#        local_carro <= (LOCAL_1 + RADAR_RANGE):
#         print(" O carro foi multado ")
#     else:
#         print("O carro não foi multado ")
# else:
#     print("O carro estava dentro da velocidade permitida.")