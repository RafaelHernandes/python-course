# Exemplo de uso dos sets

# Exemplo de uso dos sets
letras = set() # o SET armazena valores únicos, exemplo: se eu digitar a letra "a" varias vezes, vai ser sempre o mesmo "a" economiza espaço e tempo de código
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)