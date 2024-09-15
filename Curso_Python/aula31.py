"""
Flag (Bandeira) - Marcar um local

None = Não valor

is e is not = é ou não é (tipo, valor, identidade)

id = Identidade
"""

# Para caso de você criar duas variáveis diferentes com o MESMO valor, e o python entende que eles podem também ser o mesmo valor
# na memória, e sempre vai entregar o mesmo id 
v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))

# Mas se eu mudar o valor, ele muda o id
v3 = "b"
print(id(v3))

# condicao = False

# Flag

# Para o caso de você querer verificar uma condição, e você tem o seguinte cenário:

condicao = True # Aqui eu defini a variável condição um valor True
passou_no_if = None # Aqui eu defini a variável passou no if um NÃO VALOR

# Mas qual é o x da questão? se eu não declarasse o passou_no_if = None fora, e quisesse deixar algo dentro do if para validar o IF
# mas eu quisesse exibir fora do IF, como está acontecendo, se a condicao fosse False e pulasse direto para o ELSE, o código
# iria dar erro e a variavel passou_no_if não iria ser criada, então esse passou_no_if dentro do IF é apenas uma flag para mostrar
# se a condição foi verdadeira ou não

if condicao: 
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)


# Exemplos de qual seria a utilidade de uma FLAG:

# Nesse caso por ele não ter passado na condição verdadeira e o valor dele ainda ser none, você pode mandar ele executar alguma coisa
if passou_no_if is None: 
    print("Não passou no if")

# Já nesse caso por ele  ter passado na condição verdadeira e o valor dele ser True, você pode mandar ele executar outra coisa
if passou_no_if is not None:
    print("Passou no if")