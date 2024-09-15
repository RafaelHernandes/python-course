"""
Introdução ao Try/Except

try -> tentar executar o código

except - ocorreu algum erro ao tentar executar

Obs: nessa aula é somenta o básico do try/except
"""
numero_str = input("Vou dobrar o número que você digitar: ")


try:
    numero_float = float(numero_str) # o Erro vai ser nessa linha e ele vai pular para o except, caso eu digite uma letra
    # Porém invés do código ser parado bruscamente por conta desse erro, ele somente me levou a excessão que diz que não é um número
    print(f"O dobro de {numero_str} é {numero_float * 2}")
except:
    print("Isso não é um número")

# Obs: esse método do Try/Except é somente para aprender, não é prudente usar dessa forma

# if numero_str.isdigit():
#     # O método .isdigit é para verificar se o que foi digitado é somente NÚMERO e NADA MAIS
      # numero_float = float(numero_str)
      # print(f"O dobro de {numero_str} é {numero_float * 2}")
    
# else:
#     print("Isso não é um número")

# Porém esse código tem um erro, se vc digitar 2.5 ele vai dar um erro dizendo que não é um número, pois o . não é considerado número
  

    
