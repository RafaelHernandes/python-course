# Operadores lógicos - OR
# Apenas uma das condições precisam ser TRUE para executar um bloco de comando
# Ou seja, qualquer condição verdadeira avalia toda a expressão como verdadeira.

entrada = input("[E]ntrada [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

# Exemplo de OR, a utilização do parenteses faz ele checar os dois tipos de letra maiuscula e minuscula
# como uma expressão só, pois ela vai ser realizada primeiro pelo fato de estar dentro do parenteses
# se retornar uma expressão OU outra, ele vai enviar como verdadeira e vai para o AND
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida: 
 
    print("Entrar ")
else:
    print("Sair ")
    
    
# Avaliação de curto circuito (OR):

print(False or False or True ) # se QUALQUER valor for verdadeiro, a expressão toda será verdadeira