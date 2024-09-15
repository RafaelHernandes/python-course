"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    global x # ao declarar o global x, significa que o "x" que está fora do escopo da função, vai ser alterado dentro da função, obs: não é uma boa prática de programação.
    x = 10

    def outra_funcao(): # Só é possível acessar a "outra_funcao()" chamando ela de dentro da função "escopo()" e a escopo conseguimos acessar de forma externa.
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao() # Para que uma função dentro de outra seja executada, é necessário chamar ela na função de fora, só dessa forma a gente consegue acessar, chamando ela
    # na função de fora, e acessando a função que está abrangendo ela de forma externa
    print(x)


print(x)
escopo()
print(x) 