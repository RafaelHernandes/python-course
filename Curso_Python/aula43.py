# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

# o While é mais utilizado para quando não sabemos ao exato a quantidade de repetições que vão ocorrer em determinado código, nesse caso
# quando é necessário validar algo que não tenha um valor exato, um input de dados etc..

#Já o método FOR, é o mais usado para quando as variáveis são fixas.
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')