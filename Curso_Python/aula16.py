# Operações condicionais

# if / elif / else
# se / se nao se / se nao

entrada = input("Você quer 'entrar' ou 'sair' ? ")

# A forma de algum valor pertencer ao IF é apertando tab na linha abaixo dele, para que identado corretamente


if entrada == "entrar":
    print("Você entrou no sistema")
elif entrada == "sair":
    print("Você saiu do sistema")
else:
    print("Você não digitou nenhuma das opções")

print("Fora do bloco do IF")