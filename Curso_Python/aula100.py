# dir, hasattr e getattr em Python

string = "Rafael"
# metodo = "upper"

if hasattr(string, "upper"): # Verificar se a String TEM o método UPPER, se esse método existe para o tipo de dado
    print("Existe Upper")
    print(string.upper())
    
# O tipo getattr ele te permite chamar uma variável e ver se existe o método de outra variável

# if hasattr(string, metodo):
#     print('Existe upper')
#     print(getattr(string, metodo)())
# else:
#     print('Não existe o método', metodo)
