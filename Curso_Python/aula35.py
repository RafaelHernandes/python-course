"""
Parte 2

Repetições 
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop infinito -> Quando um código não tem fim
"""

contador = 0 # Declaro o valor como 0 

while contador < 10: # Enquanto o contador for menor do que 10, faça:
    contador = contador + 1 # atribuindo ao contador, o próprio valor ( que é 0 ) + 1
    print(contador) # Exibindo a contagem do 1 ao 10, porque eu estou exibindo após declarar o contador como 1
# Caso eu coloque o print antes, ele vai exibir o primeiro valor do contador (0) e vai até o 9 
# porque quando ele for validar se 10 é menor do que 10 ele vai entender que não, e exibe o ultimo valor (9)
# Mas se eu atribuir <= 10, ele vai do 0 ao 10, pois quando ele for validar se 10 é <= a 10 vai ser verdadeiro

print("Acabou")