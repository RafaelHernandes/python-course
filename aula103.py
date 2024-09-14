# Introdução às Generator Functions em Python
# generator = (n for n in range(10000))

# Função geradora (Generator Functions) =  Criar uma função que sabe pausar.

def generator(n=0): # Toda função geradora usa "yield"
    yield 1 # Pausar
    return "Acabou" # Para caso de alguem pedir o próximo valor após ter chegado ao fim, mostra um StopInteration com a mensagem "Acabou"

gen = generator(n=0)
print(next(gen))
print(next(gen)) # Exemplo do return da função.

# yield também funciona para parar o "while True:"