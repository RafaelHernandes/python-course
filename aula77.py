"""
Exercício

Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

"""
# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# digit = input("Digite um número inteiro: ")

# if digit.isdigit():
#     digit = int(digit)
#     d = duplicar(digit)
#     t = triplicar(digit)
#     q = quadruplicar(digit)
#     print(f"O número que você digitou: \n"
#           f"Duplicado: {d} \n"
#           f"Triplicado: {t} \n"
#           f"Quadruplicado: {q} \n"
#          )
# else:
#     print("O que você digitou não é um número")

# o jeito que está acima não está incorreto mas não concorda que isso é um "desperdício" de função? pois são funções muito parecidas, poderiamos fazer de um jeito que use
# Menos linhas de código, exemplo:

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar # sem o parenteses para não executar nesse momento

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2)) # Está sendo passado o segundo parâmetro da função somente na hora do print, mas da pra passar juntamente na variável também
print(triplicar(2))
print(quadruplicar(2))