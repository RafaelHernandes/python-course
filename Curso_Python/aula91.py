def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica # sem os parenteses para não executar agora.
duplica = executa(
    lambda m: lambda n: n * m, 2 # é a mesma coisa da def cria_multiplicador, porém aqui é necessario passar um parâmetro já, porém isso deixa o código complexo pois é
    # uma lambda que retorna outro lambda
)
print(duplica(2))
print(
    executa(
        lambda x, y: x + y, 2, 3 # isso é a mesma coisa que declarar a def soma
    )
)