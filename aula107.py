# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print("Abrir arquivo")
    8/0
except ZeroDivisionError:
    print("Erro de divisão por zero")
    
else: # Caso não ocorra erros
    print("Não deu erros")
finally: # O Finally SEMPRE será executado, MESMO QUE OCORRA UM ERRO.
    print("Fechar Arquivo")
    
    
# combinações: Try + Except, Try + Except + Finally, Try + Except + Else, Try + Except + Finally + Else