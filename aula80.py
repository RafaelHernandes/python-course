# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Ricardo Hernandes',
    'idade': 900,
}

pessoa.setdefault('idade', 0) # para caso de não existir uma chave e um valor que esteja sendo solicitado, e possível criar e setar um valor padrão, mas se EXISTIR O VALOR
# nada será feito.
print(pessoa['idade'])

# print(len(pessoa))
# print(list(pessoa.keys())) .keys retorna o nome de todas as chaves.
# print(list(pessoa.values())) 
# print(list(pessoa.items())) retorna as chaves e os valores, muito interessante

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)